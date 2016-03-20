from collections import namedtuple
from enum import Enum
import pprint
import json
import csv
import xlsxwriter

class Format(Enum):
    json = 1
    csv = 2
    excel = 3

Metadata = namedtuple("Metadata", "num_cols num_entries")

class Table:

    def __init__(self, data):
        """
        Stores a given table as a dictionary. The keys are the headings and the
        values are the data, represented as lists.
        """
        self.table_data = data

    def get_metadata(self):
        """
        Returns a Metadata object that contains the number of columns
        and the total number of entries.
        """

        col_headings = self.table_data.keys()
        num_cols = len(col_headings)
        num_entries = 0

        for heading in col_headings:
            num_entries += len(self.table_data[heading])

        return Metadata(
            num_cols = num_cols,
            num_entries = num_entries
        )

    def show_table(self):
        """
        Prints a formatted table to the command line using pprint
        """
        pprint.pprint(self.table_data, width=1)

    def save_table(self, format, name):
        """
        Saves a table to one of the given formats - csv, excel, and json
        under the given file name. File name should omit the extension.
        """

        # handle each case separately

        # convert to json
        if format.value == 1:
            fname = name + ".json"

            with open(fname, 'w') as outf:
                json.dump(self.table_data, outf, indent=4)

        # convert to csv
        elif format.value == 2:
            fname = name + ".csv"

            with open(fname, 'wb') as outf:
                w = csv.writer(outf)
                w.writerow(self.table_data.keys())
                w.writerows(zip(*self.table_data.values()))

        # convert to excel
        elif format.value == 3:
            fname = name + ".xlsx"

            workbook = xlsxwriter.Workbook(fname)
            worksheet = workbook.add_worksheet()

            col = 0
            for key in self.table_data.keys():
                row = 0
                worksheet.write(row, col, key)
                for item in self.table_data[key]:
                    row += 1
                    worksheet.write(row, col, item)
                col += 1

            workbook.close()
