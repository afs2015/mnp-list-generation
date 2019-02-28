import csv
import itertools
import sys
from operator import itemgetter

def main ():
    # Check if filename provided
    if len(sys.argv) > 1:
        unparsed_csv = sys.argv[1]
    else:
        unparsed_csv = 'input/SampleFile.csv'

    # Open unparsed csv
    with open(unparsed_csv) as infile:
        csv_reader = csv.reader(infile, delimiter=',')

        # Skip first three lines
        for skip in range(3):
            next(csv_reader)

        entry_list = []
        for row in csv_reader:
            entry_list.append([row[0].lower(), row[1].lower()])

        # Sort Alphabetically
        entry_list.sort(key=itemgetter(0))

        # Remove Duplicates
        # entry_list = list(entry_list for entry_list,_ in itertools.groupby(entry_list))

    # Open outfile to write to
    with open('output/output_file.csv', mode='w') as outfile:
        entry_writer = csv.writer(outfile, delimiter=',',quotechar='"')

        for entry in entry_list:
            entry_writer.writerow([entry[0], entry[1]])

if __name__== "__main__":
        main()
