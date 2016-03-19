from bs4 import BeautifulSoup
from collections import namedtuple
import urllib

class Page:

    def __init__(self, url):
        """
        Retrieves and stores the urllib.urlopen object for a given url
        """

        self.page_link = urllib.urlopen(url)

    def get_metadata(self):
        """
        Returns metadata about the tables contained in the url, which includes
        the number of tables, the number of rows, columns, and so on.
        """

        # getting the number of tables is trivial
        # just count the number of <table> tags
        html = self.page_link.read()
        parsed_html = BeautifulSoup(html, "html.parser")
        num_tables = len(parsed_html.findAll("table"))
        print num_tables



    def save_tables(self, format, names=None):
        """
        Extracts the tables from HTML and converts them to the given format
        and returns metadata about the files created
        """

        return True

    def to_dictionary(self):
        """
        Places all tables on the page into a single dictionary and returns it.
        Obviously not recommended if there's a lot of tables on a given page.
        """

        return True

if __name__ == "__main__":
    link = "http://www.w3.org/TR/html401/struct/tables.html"
    test = Page(link)
    test.get_metadata()
