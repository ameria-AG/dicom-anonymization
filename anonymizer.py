import os
import sys
import image_helper

def anonymize(input_file, output_file):
    print("Anonymizing " + input_file)
    image_helper.make_anonim_and_save_file(input_file, output_file)
    print("File saved to " + output_file)

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("Syntax error")
        print("Example:")
        print("python anonymzer.py path/to/inputfile.dicom path/to/outputfile.nii")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    anonymize(input_file, output_file)
