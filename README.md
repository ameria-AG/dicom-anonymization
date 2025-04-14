# A tool for volumetric data anonymization

This Python script takes as input a DICOM directory with potentially confidential metadata. It erases the metadata tags that contain personal information.

The output file contains only the pixel data and geometric information. Confidential metadata, such as patient name, age, etc., are discarded.

## Dependencies

* python3
* the following packages: SimpleITK

## Command-line syntax

```
python3 anonymizer.py input_dicom_file output_dicom_file
```
```
python3 anonymizer.py path/to/input/folder path/to/output/folder
```

## Exemple
```
python3 anonymizer.py example/file.dcm output.dcm
```

