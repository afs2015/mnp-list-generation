import csv
import itertools
import sys
from datetime import date
from operator import itemgetter

def create_unparsed_list(unparsed_csv, skip_flag=True):
    """ This takes in an unparsed_csv (str) and skip_flag (str)
        It returns a list of unparsed strings representing
        entries to a dance. """

    # Open unparsed csv
    with open(unparsed_csv, 'rU') as infile:
        csv_reader = csv.reader(infile, delimiter=',', dialect=csv.excel_tab)

        # Skip first three lines
        if skip_flag:
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

        # Write three rows which are header information
        current_date = date.today().strftime("%B %d, %Y")
        title_string = 'Guest list for {}'.format(current_date)
        entry_writer.writerow([title_string])
        entry_writer.writerow(['\n'])
        entry_writer.writerow(['Name', 'Notes'])

        for entry in parsed_data:
            entry_writer.writerow([entry[0], entry[1]])

    status = "The guest list file was successfully created!"

    return status

def main ():

    # Check if filename provided
    if len(sys.argv) > 2:
        guest_csv = sys.argv[2]
        unparsed_csv = sys.argv[1]
    elif len(sys.argv) > 1:
        guest_csv = 'input/guests.csv'
        unparsed_csv  = sys.argv[1]
    else:
        guest_csv = 'input/guests.csv'
        unparsed_csv  = 'input/SampleFile.csv'

    # Create list of entries to dance from .csv
    entry_list = create_unparsed_list(unparsed_csv)

    # Grab list of guests to be appended to the list
    additional_guests_list = create_unparsed_list(guest_csv, False)

    # Combine the lists
    entry_list.extend(additional_guests_list)

    # Parse list of entries to dance
    entry_list = parse_entries(entry_list)

    # Write to outfile and return status
    output = write_outfile(entry_list, get_filename_datetime())
    print(output)

if __name__== "__main__":
        main()
