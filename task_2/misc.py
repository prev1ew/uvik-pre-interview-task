import csv
from settings import csv_filename, csv_headers
from datetime import datetime


def initialize_file():
    # create a file if its non exist
    try:
        with open(csv_filename + ".csv", 'r', newline='') as csvfile:
            row_count = len(csvfile.readlines())
            if not row_count:
                writer = csv.writer(csvfile)
                writer.writerow(csv_headers)

    except:  # error while reading a file that not exists
        with open(csv_filename+".csv", 'a+', newline='') as csvfile:
            # if no rows - write headers
            writer = csv.writer(csvfile)
            writer.writerow(csv_headers)


def get_current_date():
    return datetime.today().strftime('%Y-%m-%d')