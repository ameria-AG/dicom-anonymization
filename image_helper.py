import itk

def read_image_from_dir(directory_path):
    """Reads a 3D DICOM volume from the specified directory."""
    dicom_reader = itk.ImageSeriesReader[itk.Image[itk.F, 3]].New()
    dicom_series_file_names = itk.GDCMSeriesFileNames.New()
    dicom_series_file_names.SetDirectory(directory_path)
    series_uids = dicom_series_file_names.GetSeriesUIDs()
    if not series_uids:
        raise ValueError("No DICOM series found in the specified directory.")
    print("Series file names: " + str(dicom_series_file_names.GetFileNames(series_uids[0])))
    series_file_names = dicom_series_file_names.GetFileNames(series_uids[0])
    dicom_reader.SetFileNames(series_file_names)
    dicom_reader.Update()
    dicom_image = dicom_reader.GetOutput()
    return dicom_image

def create_anonymized_image(image):
    """Creates a new ITK image and copies the pixel data from the given image."""
    image_type = type(image)
    new_image = image_type.New()
    # Set the regions, spacing, and origin to match the original image
    new_image.SetRegions(image.GetLargestPossibleRegion())
    new_image.SetSpacing(image.GetSpacing())
    new_image.SetOrigin(image.GetOrigin())
    new_image.SetDirection(image.GetDirection())
    # Allocate memory and copy pixel data
    new_image.Allocate()
    original_buffer = itk.array_view_from_image(image)
    new_buffer = itk.array_view_from_image(new_image)
    new_buffer[:] = original_buffer[:]   
    return new_image


def save_image_to_nifti(image, output_filename):
    """Saves the ITK image to a NIfTI file."""
    writer = itk.ImageFileWriter.New(image)
    writer.SetFileName(output_filename)
    writer.Update()