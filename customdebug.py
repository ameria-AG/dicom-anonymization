import os
import pydicom

folder = r"C:\Users\bmorel\Desktop\DataMRTConfidential\data1\DICOM\PAT1\STUDY1"
folder_output = r"C:\Users\bmorel\Desktop\DataMRTConfidential\data1\DICOM\PAT1\OUTPUT"
import anonymizer
series_info = {}

# Go through all subfolders and find series UIDs
anonymizer.anonymize_dir(folder, folder_output)

# Print series information
for uid, files in series_info.items():
    print(f"Series UID: {uid}, Number of Files: {len(files)}")