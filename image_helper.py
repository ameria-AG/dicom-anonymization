import os
import SimpleITK as sitk

def make_anonim_and_save_file(dicom_file, output_dicom_file):
    """Reads a 3D DICOM volume from the specified directory."""
    reader = sitk.ImageFileReader()
    reader.SetFileName(dicom_file)
    reader.LoadPrivateTagsOn()
    reader.ReadImageInformation()
    image = reader.Execute()

    for k in image.GetMetaDataKeys():
        if(k.startswith("0008") or k.startswith("0010")):
            image.EraseMetaData(k)

    output_dir = os.path.dirname(output_dicom_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    writer = sitk.ImageFileWriter()
    writer.KeepOriginalImageUIDOn()
    writer.SetFileName(output_dicom_file)
    writer.Execute(image)