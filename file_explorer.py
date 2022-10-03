import tkinter.messagebox
from tkinter import filedialog as fd
import os
import re

# initial directory to browse
INITIAL_DIR = "C:/Users/Scott/PycharmProjects/WPT/csv_to_load"


def browse_files():
    filename = fd.askopenfilename(
        initialdir=INITIAL_DIR,
        title="Select a File",
        filetypes=[("csv", ".csv")]
    )
    return filename


def rename_file_after_load(file):
    old_name = 'file'
    new_name = f"{old_name}_loaded"
    try:
        os.path.isfile(new_name)
    except FileExistsError:
        print("This file already exists.")
        print("Removing Existing file.")
        os.remove(new_name)
        os.rename(old_name, new_name)
        print("Done renaming a file.")


def filename_date_replace(df, filename):
    # sort dataframe by date created, get the first row, convert to string, and perform regex operations
    # to only get dash seperated date of first ticket by date created. return date only
    first_date_in_range = df["Date Created"].sort_values(ascending=True)
    first_date_in_range = first_date_in_range.iloc[[0]]
    first_date_in_range = str(first_date_in_range)
    first_date_in_range = re.findall("[0-9]{4}-[0-9]{2}-[0-9]{2}", first_date_in_range)
    first_date_in_range = first_date_in_range[0]
    print('====================', first_date_in_range)


    # try:
    #     # first_date_in_range = re.sub("[0-9]{8}", f"{first_date_in_range}", filename)
    #     # print("first_date_in_range", first_date_in_range)
    #     # filename = f"{first_date_in_range}"
    # except OSError:
    #     tkinter.messagebox.showerror(title="filename_replace_date", message="""
    #     Something went wrong configuring the file name. Old file name will stay the same.""")
    return first_date_in_range
