import csv
import itertools
import sys
from datetime import date
from operator import itemgetter

def create_unparsed_list(unparsed_csv):
    """ This takes in an unparsed_csv (str) and returns a list of
        unparsed strings representing entries to a dance. """

    # Open unparsed csv
    with open(unparsed_csv) as infile:
        csv_reader = csv.reader(infile, delimiter=',')

        # Skip first three lines
        for skip in range(3):
            next(csv_reader)

        entry_list = []
        for row in csv_reader:
            entry_list.append([row[0].lower(), row[1].lower()])

    return entry_list

def get_filename_datetime():
    """ Use current date to get a text file name. Returns a (str) """

    filename = "BLH-entry-list_{}.csv".format(date.today())
    return filename

def parse_entries(entry_list):
    """ Takes in unparsed_csv (list), runs some parsing tasks, and
        returns a parsed_list (list) """

    # Sort Alphabetically
    entry_list.sort(key=itemgetter(0))

     # Remove Duplicates
    parsed_list = list(entry_list for entry_list,_ in itertools.groupby(entry_list))

    return parsed_list

def write_outfile(parsed_data, outfile):
    """ Takes in parsed_data (list) and outfile (str).
        It writes to a file and returns a status(str). """

    # Open outfile to write to
    with open(outfile, mode='w') as outfile:
        entry_writer = csv.writer(outfile, delimiter=',',quotechar='"')

        for entry in parsed_data:
            entry_writer.writerow([entry[0], entry[1]])

    status = "The entrance file was successfully created!"

    return status

def main ():

    # Check if filename provided
    if len(sys.argv) > 1:
        unparsed_csv  = sys.argv[1]
    else:
        unparsed_csv  = 'input/SampleFile.csv'

    # Create list of entries to dance from .csv
    entry_list = create_unparsed_list(unparsed_csv)

    # Parse list of entries to dance
    entry_list = parse_entries(entry_list)

    # Write to outfile and return status
    output = write_outfile(entry_list, get_filename_datetime())
    print(output)

if __name__== "__main__":
        main()
