import urllib
from collections import namedtuple
from enum import Enum

class DataFormat(Enum):
    csv = 1
    excel = 2
    json = 3
    txt = 4

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

    def save_table(self, format, name):
        """
        Saves a table to one of the given formats - csv, excel, json, and txt
        under the given file name. File name should omit the extension.
        """
        

    def display_table(self):
        """
        Prints a formatted table to the command line
        """

if __name__ == "__main__":
    table = {"cars":["mercedes", "honda"], "fruits":["apple", "pear"]}
    table_obj = Table(table)
