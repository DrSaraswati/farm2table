# import our library
from farm2table import *

# url that contains the tables we want
url = "https://coinmarketcap.com/exchanges/volume/24-hour/"

# convert to a page object
page = Page(url)

# get the tables
tables = page.get_tables()

# save the tables
page.save_tables(tables)

# you can change the name that it saves the table to by calling save_table on the table object itself:
# don't include the extension in the file name
tables[0].save_table("customName")

# Sometimes, websites use HTML tables to format their page, not represent data
# You can use the ignore_small argument to handle this issue to some extent:

# Note that the below code overwrites the table1.csv file that was created from the earlier url
# https://coinmarketcap.com/exchanges/volume/24-hour/

# This website is a good example of table fragments
url = "https://www.eia.gov/electricity/monthly/epm_table_grapher.cfm?t=epmt_1_1"
page = Page(url)
tables = page.get_tables()
page.save_tables(tables, ignore_small=False)

# Because we included the ignore_small=True part, any small tables will not be saved. 
# As a result, layout elements are usually ignored. It's not a perfect fix, but it's good for now.