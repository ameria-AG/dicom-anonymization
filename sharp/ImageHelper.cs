using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Security.Policy;
using itk.simple;
using static System.Net.WebRequestMethods;

namespace WindowsFormsApp1
{
    internal class ImageHelper
    {

        public static void SupressItkWarning()
        {
            ProcessObject.SetGlobalWarningDisplay(false);
        }

        public static List<string> FindDicomFiles(string dir)
        {
            var fileNames = ImageSeriesReader.GetGDCMSeriesFileNames(dir);
            return fileNames.ToList();
        }

        public static void MakeAnonimAndSaveFile(string filename, string outputFile)
        {
            //Reads a 3D DICOM volume from the specified directory.
            ImageFileReader reader = new ImageFileReader();
            reader.SetFileName(filename);
            reader.LoadPrivateTagsOn();
            var image = reader.Execute();

            foreach (var key in image.GetMetaDataKeys())
            {
                if (key.StartsWith("0008") || key.StartsWith("0010"))
                {
                    image.EraseMetaData(key);
                }
            }

            var path = Path.GetDirectoryName(outputFile);
            if (!Directory.Exists(path))
            {
                Directory.CreateDirectory(path);
            }

            var writer = new ImageFileWriter();
            writer.KeepOriginalImageUIDOn();
            writer.SetFileName(outputFile);
            writer.Execute(image);
        }
        
        public static void AnonymizeFile(string filename, string outputFile) 
        {
            if (Path.GetExtension(outputFile) != ".dcm")
            {
                outputFile += ".dcm";
            }

            MakeAnonimAndSaveFile(filename, outputFile);
        }

        public static int AnonymizeDir(string dir, string outputDir)
        {
            dir = Path.GetFullPath(dir);
            int fileCount = 0;

            var dicomFiles = FindDicomFiles(dir);
            foreach (var dicom in dicomFiles)
            {
                var inputFile = Path.GetFileName(dicom);
                var relPath = dir.Substring(dir.Length - 1);
                var outputFile = Path.Combine(outputDir, relPath, inputFile);
                AnonymizeFile(inputFile, outputFile);
            }

            foreach (var subdir in Directory.EnumerateDirectories(dir, "*", SearchOption.AllDirectories))
            {
                dicomFiles = FindDicomFiles(subdir);
                foreach (var dicom in dicomFiles)
                {
                    var inputFile = Path.GetFullPath(dicom);
                    var relPath = inputFile.Substring(dir.Length);
                    var outputFile = outputDir + relPath;
                    AnonymizeFile(inputFile, outputFile);
                    fileCount++;
                }
            }
            return fileCount;
        }
    }
}
