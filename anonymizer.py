import os
import sys
import image_helper

def anonymize(input_file, output_file):
    filename, output_file_ext = os.path.splitext(output_file)
    if output_file_ext != ".dcm":
        output_file = output_file + ".dcm"

    print("Anonymizing " + input_file)
    image_helper.make_anonim_and_save_file(input_file, output_file)
    print("File saved to " + output_file)

def anonymize_dir(input_dir, output_dir):
    for root, _, files in os.walk(input_dir):
        dicom_files = image_helper.find_dicom_files_in_dir(root)
        for file in dicom_files:
            rel_path = os.path.relpath(root, input_dir)
            file_name = os.path.basename(file)
            input_file_name = os.path.join(root, file_name)
            output_file_name = os.path.normpath(os.path.join(output_dir, rel_path, file_name))
            anonymize(input_file_name, output_file_name)

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("Syntax error")
        print("Example:")
        print("python3 anonymizer.py path/to/inputfile.dcm path/to/outputfile.dcm")
        print("python3 anonymizer.py path/to/input/folder path/to/output/folder")
        sys.exit(1)
    input = sys.argv[1]
    output = sys.argv[2]

    if os.path.isfile(input):
        anonymize(input, output)

    if os.path.isdir(input):
        anonymize_dir(input, output)
