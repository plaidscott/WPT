import os
import tkinter
from tkinter import messagebox


def filter_jsi_only(df):
    # filter for jsi load tickets
    jsi_load_rows = df[df['Subject'].str.contains('[0-99]\\-[0-9999]|JSI', case=False, regex=True)]
    # print("jsi_load_rows", jsi_load_rows)
    return jsi_load_rows


def calculate_gb_processed(jsi_tickets):
    total_gb = jsi_tickets['Data Processed'].dropna()
    # print("total_GB:", total_GB.sum())
    total_gb = total_gb.sum()
    return total_gb


def calculate_mb_to_gb(mb):
    return mb / 1000


def average(sum, count):
    return round(sum / count)


def count_tickets(tickets):
    return tickets["Ticket Number"].count()


def sum_time(tickets):
    return tickets["Time Spent"].dropna().sum()


def file_creation(folder_path, file_name, df):
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path, exist_ok=True)
        except FileNotFoundError:
            tkinter.messagebox.showerror(title=f"File creation error", message="""
            Something went wrong creating the file. The file path may not exist
            """)
    else:
        # print('it does exist')
        try:
            df.to_excel(f"{folder_path}/{file_name}.xlsx")

        except FileExistsError:
            tkinter.messagebox.showerror(title=f"File creation error", message="""
            Something went wrong creating the file. The file path exists but something
            else went wrong.
            """)
