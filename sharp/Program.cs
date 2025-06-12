using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    internal static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            UnpackEmbeddedDll();

            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
        }

        private static void UnpackEmbeddedDll()
        {
            var assembly = Assembly.GetExecutingAssembly();
            //Getting names of all embedded resources
            var resourceDll = assembly.GetManifestResourceNames().FirstOrDefault(x => x.IndexOf("SimpleITKCSharpNative") > 0);
            var DllName = resourceDll.Substring(resourceDll.IndexOf('.') + 1);
            var pathToFile = Path.Combine(Path.GetDirectoryName(AppDomain.CurrentDomain.BaseDirectory), DllName);

            using (var stream = assembly.GetManifestResourceStream(resourceDll))
            using (var fileStream = File.Create(pathToFile))
            {
                stream.Seek(0, SeekOrigin.Begin);
                stream.CopyTo(fileStream);
            }
        }
    }
}
