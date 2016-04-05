from bs4 import BeautifulSoup
from collections import namedtuple
from Table import *
import urllib
import re

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
                    # fix the encoding issues with utf-8
                    entry = entry.text.encode("utf-8", "ignore")
                    strip_unicode = re.compile("([^-_a-zA-Z0-9!@#%&=,/'\";:~`\$\^\*\(\)\+\[\]\.\{\}\|\?\<\>\\]+|[^\s]+)")
                    entry = strip_unicode.sub(" ", entry)
                    value_list.append(entry)
                # we don't want empty data packages
                if len(value_list) > 0:
                    table_dict[count] = value_list
                    count += 1

            table_obj = Table(table_dict)
            table_list.append(table_obj)

        return table_list

    def save_tables(self, tables, ignore_small=False):
        """
        Takes an input a list of table objects and saves each
        table to csv format. If ignore_small is True,
        we ignore any tables with 5 entries or fewer. 
        """

        counter = 1
        for table in tables:
            if ignore_small:
                if table.get_metadata().num_entries > 5:
                    name = "table" + str(counter)
                    table.save_table(name)
                    counter += 1
            else:
                name = "table" + str(counter)
                table.save_table(name)
                counter += 1

