import anonymizer

folder = r"C:\Users\bmorel\Desktop\DataMRTConfidential\data1\DICOM\PAT1\STUDY1"
folder_output = r"C:\Users\bmorel\Desktop\DataMRTConfidential\data1\DICOM\PAT1\OUTPUT"

no_ext_file = r"C:\Projects\Dicom_Anonim\example\Test\DICOM\PAT1\STUDY1\SERIES1\INST_no_ext"
no_ext_file_out = r"C:\Projects\Dicom_Anonim\example\Test\DICOM\PAT1\Output\INST_no_ext"
series_info = {}

# Go through all subfolders and find series UIDs
#anonymizer.anonymize(no_ext_file, no_ext_file_out)
anonymizer.anonymize_dir(folder, folder_output)

# Print series information
for uid, files in series_info.items():
    print(f"Series UID: {uid}, Number of Files: {len(files)}")