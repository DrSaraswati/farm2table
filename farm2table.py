from bs4 import BeautifulSoup
from collections import namedtuple
from enum import Enum
from Table import *
import urllib

class Format(Enum):
    json = 1
    csv = 2
    excel = 3

class Page:

    def __init__(self, url):
        """
        Retrieves and stores the urllib.urlopen object for a given url
        """

        self.link = urllib.urlopen(url)

    def get_tables(self):
        """
        Extracts each table on the page and places it in a dictionary.
        Converts each dictionary to a Table object. Returns a list of
        pointers to the respective Table object(s).
        """

        raw_html = self.link.read()
        soup = BeautifulSoup(raw_html, "html.parser")
        tables = soup.findAll("table")

        # have to extract each entry using nested loops
        table_list = []
        for table in tables:
            # empty dictionary each time represents our table
            table_dict = {}
            rows = table.findAll("tr")
            # count will be the key for each list of values
            count = 0
            for row in rows:
                value_list = []
                entries = row.findAll("td")
                for entry in entries:
                    value_list.append(entry.text.strip())
                if len(value_list) > 0:
                    table_dict[count] = value_list
                    count += 1

            table_obj = Table(table_dict)
            table_list.append(table_obj)

        return table_list

    def save_tables(self, tables, format):
        """
        Takes an input a list of table objects and saves each
        to the given format, either json, csv, or excel
        """

        counter = 1
        for table in tables:
            name = "table" + str(counter)
            table.save_table(format, name)
            counter += 1


if __name__ == "__main__":
    url = "https://www.eia.gov/forecasts/steo/report/renew_co2.cfm"
    page = Page(url)
    tables = page.get_tables()
    page.save_tables(tables, Format.excel)
