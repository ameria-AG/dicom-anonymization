SENSITIVE_TAGS_STRING = {
    "0010|0010",  # Patient's Name
    "0010|0020",  # Patient ID
    "0010|0040",  # Patient's Sex
    "0010|0050",  # Insurance Plan Code Sequence
    "0010|1000",  # Other Patient IDs
    "0010|1001",  # Other Patient Names
    "0010|1090",  # Medical Record Locator
    "0010|2160",  # Ethnic Group
    "0010|2180",  # Occupation
    "0010|21B0",  # Additional Patient History
    "0008|0050",  # Accession Number
    "0020|0010",  # Study ID
    "0032|1032",  # Requesting Physician
    "0032|1033",  # Requesting Service
    "0008|0090",  # Referring Physician's Name
    "0008|0092",  # Referring Physician's Address
    "0008|0094",  # Referring Physician's Phone Numbers
    "0008|1048",  # Physician(s) of Record
    "0008|1060",  # Reading Physician's Name
    "0008|1070",  # Operator's Name
    "0008|0080",  # Institution Name
    "0008|0081",  # Institution Address
    "0008|1040",  # Institutional Department Name
    "0008|1010",  # Station Name
    "0008|1090",  # Manufacturer's Model Name
    "0018|1004",  # Plate ID
    "0018|1010",  # Secondary Capture Device ID
    "0018|1018",  # Protocol Name
    "0008|1030",  # Study Description
    #"0008|103E",  # Series Description
    "0018|1030",  # Protocol Name
    "0040|0254",  # Performed Procedure Step Description
    "0040|0253",  # Performed Procedure Step ID
    "0032|4000",  # Study Comments
    "0010|4000",  # Patient Comments
    "4008|0040",  # Results Comments
    "0040|4000",  # Identifying Comments
}

SENSITIVE_TAGS_DATE = {
    "0010|0030",  # Patient Birth Date
    "0008|0020",  # Study Date
    "0008|0021",  # Series Date
    "0008|0022",  # Acquisition Date
    "0008|0023",  # Content Date
    "0040|0244",  # Procedure Step Start Date
}

SENSITIVE_TAGS_TIME = {
    "0010|0032",  # Patient Birth Time
    "0008|0030",  # Study Time
    "0008|0031",  # Series Time
    "0008|0032",  # Acquisition Time
    "0008|0033",  # Content Time
    "0040|0245",  # Procedure Step Start Time
}

SENSITIVE_TAGS_UID = {
    "0020|000D",  # Study Instance UID
    "0020|000E",  # Series Instance UID
    "0008|0018",  # SOP Instance UID (not in original list but often included)
    "0040|A124",  # UID in Content Item
    "0020|0052",  # Frame of Reference UID
}

SENSITIVE_TAGS_UINT = {
    "0010|1010",  # Patient's Age
    "0010|1020",  # Patient's Size
    "0010|1030",  # Patient's Weight
    "0010|21C0",  # Pregnancy Status
}

SENSITIVE_TAGS_OTHER = {
    "0032|1000",  # Requesting Physician Identification Sequence
    "0008|1072",  # Operator Identification Sequence
    "0018|1000",  # Device Serial Number
    "0040|A730",  # Content Sequence
}