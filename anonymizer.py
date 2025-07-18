import os
import sys
import image_helper
from window import create_window, show_info
from tag_anonymizer import TagAnonymizer

def anonymize_file(input_file, output_file, anonyizer: TagAnonymizer):
    filename, output_file_ext = os.path.splitext(output_file)
    if output_file_ext != ".dcm":
        output_file = output_file + ".dcm"

    print("Anonymizing " + input_file)
    image_helper.make_anonim_and_save_file(input_file, output_file, anonyizer)
    print("File saved to " + output_file)

def anonymize_dir(input_dir, output_dir, anonyizer: TagAnonymizer):
    files_anonymized = 0
    for root, _, files in os.walk(input_dir):
        dicom_files = image_helper.find_dicom_files_in_dir(root)
        for file in dicom_files:
            rel_path = os.path.relpath(root, input_dir)
            file_name = os.path.basename(file)
            input_file_name = os.path.join(root, file_name)
            output_file_name = os.path.normpath(os.path.join(output_dir, rel_path, file_name))
            anonymize_file(input_file_name, output_file_name, anonyizer)
            files_anonymized+=1
    return files_anonymized


def anonymize(input, output):
    anonymizer = TagAnonymizer()
    if os.path.isfile(input):
        if os.path.isdir(output):
            output = os.path.join(output, os.path.basename(input))
        anonymize_file(input, output, anonymizer)
        show_info("File saved to " + os.path.normpath(output))

    if os.path.isdir(input):
        files_count = anonymize_dir(input, output, anonymizer)
        show_info(str(files_count) + " files saved to " + os.path.normpath(output))

if __name__ == "__main__":
    defaultDir = os.path.dirname(sys.executable)
    defaultOutputDir = os.path.join(defaultDir, "Output")
    if (len(sys.argv) > 2):
        defaultDir = sys.argv[1]
        defaultOutputDir = sys.argv[2]
    create_window(defaultDir, defaultOutputDir, anonymize)
