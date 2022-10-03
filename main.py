# pre-made modules
import pandas as pd
from datetime import datetime

# custom modules
from file_explorer import *
from file_processing_functions import *

# option sto set how pandas display rows/columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Filepaths
year_month_day = datetime.now()
year_month_day = year_month_day.strftime("%Y%m%d")
CSV_NAME = ''


# FOR TESTING*********
# REMOVE WHEN DONE TESTING**************
# Uncomment filename variable further down imported from browse
filename = "C:/Users/Scott/PycharmProjects/WPT/csv_to_load/Closed Tickets - 20220301.csv"
REPORT_FOLDER_PATH = f"C:/Users/Scott/PycharmProjects/WPT/WPT_Reports"

# INPUT a new csv file from file explorer
# filename = browse_files()

# load file to data frame
df = pd.read_csv(filename, index_col=None, header=0)
# print(df.head(30))

# first date of ticket to append to report name
# Grabs the first row of ascending values for dates. Should be the first date in that dataframes date range
# Returns new filename with date replacing old date in filename
CSV_NAME = filename_date_replace(df, filename)
print("filename\n+++++++++++++\n", CSV_NAME)

# filter for only rows containing text for jsi, or for case title format ##-####
jsi_tickets = filter_jsi_only(df)
print(jsi_tickets.head(2))

# calculate GB processed on JSI tickets input MB output GB
# Drop NaN rows
processed_data = calculate_gb_processed(jsi_tickets)
# print("processed_data: ", processed_data)

# calculate MB to GB conversion
total_GB = calculate_mb_to_gb(processed_data)
total_GB = round(total_GB)
# print(total_GB)

# avg time spent per ticket
total_tickets = count_tickets(df)
# print("total_tickets:", total_tickets)
total_minutes = sum_time(df)
# print("total_minutes:", total_minutes)
avg_min_per_ticket = average(total_minutes, total_tickets)
# print("avg_min_per_ticket: ", avg_min_per_ticket)

# create new data frame
report = {
    'total_tickets': [total_tickets],
    'avg_ticket_time': [avg_min_per_ticket],
    'total_gb': [total_GB]
}
df_report = pd.DataFrame(report)
print(df_report)

# check for directory existing
# check for file existing
# throw errors if program cannot create for some reason
print("CSV_NAME", CSV_NAME)
file_creation(REPORT_FOLDER_PATH, CSV_NAME, df_report)
# rename_file_after_load(filename)
