import tkinter
from tkinter import messagebox


def check_for_files(filename):
    assert len(filename) == 0, tkinter.messagebox.showerror(title="File Input Error", message=f"""
        WPT_report program did not detect any csv files.
            1. Check that the file is a csv

        *The program will now shut down.*
        """)
