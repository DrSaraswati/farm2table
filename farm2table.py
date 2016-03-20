from bs4 import BeautifulSoup
from collections import namedtuple
from Table import *
import urllib

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

    def get_info(self):
        """
        Returns metadata about the tables contained in the url, which includes
        the number of tables, the number of rows, columns, and so on.
        """


    def save_tables(self, tables, format, names):
        """
        Extracts the tables from HTML and converts them to the given format
        and returns metadata about the files created
        """

        return True


if __name__ == "__main__":
    url = "https://datatables.net/examples/data_sources/dom.html"
    page = Page(url)
    page.get_tables()
