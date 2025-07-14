import os
import SimpleITK as sitk
from tag_anonymizer import TagAnonymizer


def is_metadata_sensitive(key):
    return (key.startswith("0008") or key.startswith("0010"))

def make_anonim_and_save_file(dicom_file, output_dicom_file, anonymizer: TagAnonymizer):
    """Reads a 3D DICOM volume from the specified directory."""
    reader = sitk.ImageFileReader()
    reader.SetFileName(dicom_file)
    reader.LoadPrivateTagsOn()
    reader.ReadImageInformation()
    image = reader.Execute()

    image = anonymizer.anonymize_image(image)

    output_dir = os.path.dirname(output_dicom_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    writer = sitk.ImageFileWriter()
    writer.KeepOriginalImageUIDOn()
    writer.UseCompressionOn()
    writer.SetFileName(output_dicom_file)
    writer.Execute(image)

def find_dicom_files_in_dir(directory):
    reader = sitk.ImageSeriesReader()
    series_found = reader.GetGDCMSeriesIDs(directory)
    dicom_files = []
    if series_found:
        for series in series_found:
            # Get the Dicom filename corresponding to the current series
            dicom_files += reader.GetGDCMSeriesFileNames(directory, series)

    return dicom_files
