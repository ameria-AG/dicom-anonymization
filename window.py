import os.path
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

import image_helper


def check_dicom_file_or_dir(path):
    dicom_found = False
    message = ""
    if os.path.isfile(path):
        filename, input_file_ext = os.path.splitext(path)
        if input_file_ext == ".dcm":
            dicom_found = True
        else:
            message = "Input file is not .dcm"

    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            dicom_files = image_helper.find_dicom_files_in_dir(root)
            if len(dicom_files) > 0:
                dicom_found = True
                break;
        if not dicom_found:
            message = "No .dcm files in input directory"

    return dicom_found, message

def check_button_status(execute_button, input_path_box, output_path_box, output_label):
    input_path = input_path_box.get()
    input_path_valid, message = check_dicom_file_or_dir(input_path)
    output_path = output_path_box.get()
    output_path_valid = os.path.isdir(output_path)

    if input_path_valid and output_path_valid:
        execute_button["state"] = "normal"
        show_info("Click 'Anonymize' button to start")
        #output_label["text"] = "Click 'Anonymize' button to start"
    else:
        execute_button["state"] = "disabled"
        if not input_path_valid:
            show_info(message)
            #output_label["text"] = message
        else:
            if not output_path_valid:
                show_info("Select output path")
                #output_label["text"] = "Select output path"


def open_file(input_path_box):
    filetypes = [('DCM files', '*.dcm'), ]
    initialDir = input_path_box.get()
    if not initialDir:
        initialDir = os.path.curdir
    filename = filedialog.askopenfilename(initialdir = initialDir, filetypes=filetypes)
    if filename:
        input_path_box.delete(0, tk.END)
        input_path_box.insert(tk.END, filename)

def open_dir(input_path_box):
    initialDir = input_path_box.get()
    if not initialDir:
        initialDir = os.path.curdir
    path = filedialog.askdirectory(initialdir = initialDir)
    if path:
        input_path_box.delete(0, tk.END)
        input_path_box.insert(tk.END, path)

root = tk.Tk()
output_label = ttk.Label(root, text="", relief=tk.SUNKEN)

def show_info(text):
    #global output_label
    output_label["text"] = text

def create_window(default_path, default_output_path, _start_anonymize):

    #root = tk.Tk()
    root.title('Anonymizer')
    root.geometry('500x250')
    root.resizable(width=False, height=False)

    execute_button = ttk.Button(root, text="Anonymize", command= lambda: _start_anonymize(path_entry1.get(), path_entry2.get()))
    #output_label = ttk.Label(root, text="", relief=tk.SUNKEN)

    info_label = ttk.Label(root, text="Select file or directory", anchor="center")
    info_label.pack(pady=(10, 0), fill="x")

    path_label = ttk.Label(root, text="Input path:")
    path_label.pack(pady=(10, 0), padx=20, fill="x")

    input_path_frame = ttk.Frame(root)
    input_path_frame.pack(fill="x")

    output_path_frame = ttk.Frame(root)
    output_path_frame.pack(fill="x")

    path_entry1 = ttk.Entry(input_path_frame, width=50)
    path_entry2 = ttk.Entry(output_path_frame, width=50)
    path_entry1.insert(tk.END, default_path)
    path_entry1.pack(pady=(10,0), padx=20, fill="x", side="left")

    browse_file_button = ttk.Button(input_path_frame, text="Browse file", command= lambda: {open_file(path_entry1),
                                    check_button_status(execute_button, path_entry1, path_entry2, output_label)})
    browse_file_button.pack(pady=(10,0), padx=0, side="left")

    browse_dir_button = ttk.Button(input_path_frame, text="Browse dir", command= lambda: {open_dir(path_entry1),
                                    check_button_status(execute_button, path_entry1, path_entry2, output_label)})
    browse_dir_button.pack(pady=(10, 0), padx=0, side="left")

    out_path_label = ttk.Label(root, text="Output path:")
    out_path_label.pack(pady=(10, 0), padx=20, fill="x")

    path_entry2.insert(tk.END, default_output_path)
    path_entry2.pack(pady=(10, 0), padx=20, fill="x", side="left")

    browse_button2 = ttk.Button(output_path_frame, text="Browse", command= lambda: {open_dir(path_entry2),
                                    check_button_status(execute_button, path_entry1, path_entry2, output_label)})
    browse_button2.pack(pady=(10, 0), padx=0, side="left")

    execute_button.pack(pady=(10,0), side="bottom")

    output_label.pack(pady=(10, 0), padx=20, fill="x")

    check_button_status(execute_button, path_entry1, path_entry2, output_label)

    root.mainloop()