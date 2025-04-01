import os
import sys
import image_helper

def anonymize(input_file, output_file):
    print("Anonymizing " + input_file)
    img = image_helper.read_image_from_dir(input_file)
    print(f"Image Size: {img.GetLargestPossibleRegion().GetSize()}")
    print(f"Image Spacing: {img.GetSpacing()}")
    print(f"Image Origin: {img.GetOrigin()}")
    new_img = image_helper.create_anonymized_image(img)
    image_helper.save_image_to_nifti(new_img, output_file)
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
