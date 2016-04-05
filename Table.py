from collections import namedtuple
from enum import Enum
import pprint
import json
import csv
import xlsxwriter


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

    def save_table(self, name):
        """
        Saves a table to csv format under the given file name. 
        File name should omit the extension.
        """
        fname = name + ".csv"

        with open(fname, 'wb') as outf:
            w = csv.writer(outf, dialect="excel")
            li = self.table_data.values()
            w.writerows(li)
