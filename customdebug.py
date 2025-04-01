import os
import pydicom

folder = r"C:\Users\bmorel\Desktop\DataMRTConfidential\data1\DICOM\PAT1\STUDY1"
series_info = {}

# Go through all subfolders and find series UIDs
for root, _, files in os.walk(folder):
    for file in files:
        if file.endswith(".dcm"):
            dicom_file = os.path.join(root, file)
            ds = pydicom.dcmread(dicom_file)
            series_uid = ds.SeriesInstanceUID
            if series_uid not in series_info:
                series_info[series_uid] = []
            series_info[series_uid].append(dicom_file)

# Print series information
for uid, files in series_info.items():
    print(f"Series UID: {uid}, Number of Files: {len(files)}")