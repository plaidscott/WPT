import os
import tkinter
import xlsxwriter
import glob
import pandas as pd
from tkinter import messagebox
from os.path import exists
from datetime import datetime

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#Filepaths
SOURCE_FOLDER = './csv_to_load'
WORKBOOK_PATH = f"{datetime.today().strftime('%Y_WPT_REPORT')}"

#TODO search through folder to find csv files, keep separated by week
#import csv file
#Folder Path

all_files = glob.glob(SOURCE_FOLDER + "/*.csv")

#handle a now csv file in SOURCE_FOLDER
assert len(all_files) > 0, tkinter.messagebox.showerror(title="File Input Error", message=f"""
    WPT_report program did not detect any csv files.
        1. Check that the csv is in {SOURCE_FOLDER}
        2. Check that the file in {SOURCE_FOLDER} is a csv 
    
    *The program will now shut down.*
    """)

for filename in all_files:
    print('filename:', filename)
    df = pd.read_csv(filename, index_col=None, header=0)
    print(df.head(10))

        # #filter for jsi load tickets
        # jsi_load_rows = df[df['Subject'].str.contains('[0-99]\\-[0-9999]|JSI', case=False, regex=True)]
        # # print(jsi_load_rows)
        # jsi_load_count = len(jsi_load_rows)
        # # print(jsi_load_count)
        #
        # #calculate GB processed on JSI tickets
        # #Input MB, output GB, filter for any rows without time spend
        # jsi_data_processed_col = jsi_load_rows['Data Processed']
        # jsi_with_data = jsi_data_processed_col.dropna()
        # jsi_ticket_count = jsi_with_data.count()
        # jsi_gb = jsi_with_data.sum()
        # total_gb = round(jsi_gb/1000)
        # print(f"Total GB processed for JSI: {total_gb}, from {jsi_ticket_count} cases. Averaging {total_gb/jsi_ticket_count} GBs per case.")

        #time spent on tickets (all tickets)
        #drop anything that doesnt have a time
        # time_per_ticket = df['Time Spent']
        # print(time_per_ticket)
        # time_per_ticket = time_per_ticket.dropna()
        # print(time_per_ticket['Time Spent.1'].to_string())
        # avg_ticket_time = round(time_per_ticket.sum()/time_per_ticket.count())

        # #total tickets
        # total_tickets = df['Closed Date'].count()
        # print(f'For this time period, MIS processed a total of {total_tickets} tickets.')
        #
        #
        # #create new data frame
        # report = {
        #     'total_tickets': [total_tickets],
        #     'avg_ticket_time': [avg_ticket_time],
        #     'total_gb': [total_gb]
        # }
        # df_report = pd.DataFrame(report)
        # print(df_report)
        #
        # #TODO worksheet creations
        # #construct workbook name
        #
        #
        # #construct sheet name
        # time_now = datetime.now()
        # time_now = time_now.strftime("%Y%m%d")
        # worksheet_name = f"./WPT_Reports/{time_now}_WPT_REPORT"
        #
        #
        #
        # #TODO workbook check, and append worksheet
        # if os.path.exists(WORKBOOK_PATH):
        #     print('it does exist')
        # else:
        #     df_report.to_excel(WORKBOOK_PATH, sheet_name=worksheet_name, engine='xlsxwriter')
        #
        #
        #
        #
        #
        # # df_report.to_excel(f"{time_now}_WPT_REPORT")


