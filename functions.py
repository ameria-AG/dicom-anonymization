import os
import pydicom
import io

import numpy as np
from pydicom.dataset import Dataset, FileDataset
from pydicom.uid import generate_uid

def read_dicom_series(directory_path):
    """Reads all DICOM files from the specified directory and returns them as a sorted list."""
    dicom_files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith('.dcm')]

    if not dicom_files:
        raise ValueError("No DICOM files found in the specified directory.")

    # Read and sort slices by ImagePositionPatient if available
    dicom_series = [pydicom.dcmread(f) for f in dicom_files]
    dicom_series.sort(key=lambda ds: float(ds.ImagePositionPatient[2]) if "ImagePositionPatient" in ds else 0)

    return dicom_series

def create_clean_dicom(original_dicom):
    """Creates a new clean DICOM file with only necessary metadata and pixel data."""
    new_ds = FileDataset(None, {}, file_meta=pydicom.dataset.FileMetaDataset(), preamble=b"\0" * 128)

    # Copy only essential metadata
    new_ds.Modality = original_dicom.Modality
    new_ds.Rows = original_dicom.Rows
    new_ds.Columns = original_dicom.Columns
    new_ds.PixelSpacing = original_dicom.PixelSpacing
    new_ds.SliceThickness = getattr(original_dicom, "SliceThickness", "1.0")  # Default if missing
    new_ds.ImagePositionPatient = getattr(original_dicom, "ImagePositionPatient", [0, 0, 0])
    new_ds.ImageOrientationPatient = getattr(original_dicom, "ImageOrientationPatient", [1, 0, 0, 0, 1, 0])

    # Assign new UIDs to prevent linking to the original dataset
    new_ds.StudyInstanceUID = generate_uid()
    new_ds.SeriesInstanceUID = generate_uid()
    new_ds.SOPInstanceUID = generate_uid()
    new_ds.InstanceNumber = original_dicom.InstanceNumber

    # Copy pixel data
    new_ds.PhotometricInterpretation = original_dicom.PhotometricInterpretation
    new_ds.SamplesPerPixel = original_dicom.SamplesPerPixel
    new_ds.BitsAllocated = original_dicom.BitsAllocated
    new_ds.BitsStored = original_dicom.BitsStored
    new_ds.HighBit = original_dicom.HighBit
    new_ds.PixelRepresentation = original_dicom.PixelRepresentation
    new_ds.PixelData = original_dicom.PixelData

    return new_ds

def anonymize_and_save_dicom_series(dicom_series, output_directory):
    """Creates a clean version of the DICOM series and saves them in a new directory."""
    os.makedirs(output_directory, exist_ok=True)

    for i, ds in enumerate(dicom_series):
        clean_ds = create_clean_dicom(ds)
        output_path = os.path.join(output_directory, f"anon_{i:04d}.dcm")
        clean_ds.save_as(output_path)

    print(f"Anonymized DICOM saved to {output_directory}")
