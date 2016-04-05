from farm2table import *

url = "https://coinmarketcap.com/exchanges/volume/24-hour/"
page = Page(url)
tables = page.get_tables()
page.save_tables(tables)