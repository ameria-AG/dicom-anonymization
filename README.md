# A tool for volumetric data anonymization

This Python script takes as input a DICOM directory with potentially confidential metadata. It extracts the pixel data and geometric information (bounding box, spacing, position, orientation) and stores this information in NIfTI format.

The output file contains only the pixel data and geometric information. Confidential metadata, such as patient name, age, etc., are discarded.

## Dependencies

* python3
* the following packages: itk

## Command-line syntax

```
python3 anonymizer.py input_dicon_dir output_nifti_file
```

## Exemple
```
python3 anonymizer.py example/ output.nii 
```

