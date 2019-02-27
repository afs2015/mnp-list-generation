import csv
import sys

def main ():
    # Check if filename provided
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = 'input/SampleFile.csv'

    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            print(row)
