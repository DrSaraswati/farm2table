from bs4 import BeautifulSoup
import urllib

class Page:

    def __init__(self, url):
        """
        Retrieves and stores the urllib.urlopen object for a given url
        """

        self.page_data = urllib.urlopen(url)

    def get_table_data(self):
        """
        Returns metadata about the tables contained in the url, such as the
        number of tables, the number of rows, columns, and so on.
        """
        return True

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
