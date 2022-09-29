from tkinter import *
from tkinter import filedialog as fd

def browse_files():
    filename = fd.askopenfilename(
        initialdir="C:/Users/Scott/PycharmProjects/WPT\csv_to_load",
        title="Select a File",
        filetypes=[("csv", ".csv")]
    )
    return filename
