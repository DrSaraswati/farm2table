# farm2table
Seamlessly extract HTML tables from websites and convert them to CSV with Python.

## Installation

It (will) be on PyPI so you can install farm2table with:
```
pip install farm2table
```

## Explanation
farm2table arose out of a need to extract HTML tables from websites without coding up a scraper each time. With this library, you can automatically extract each table from a given website and save them to csv files without much trouble. 

For every table on a given website (delineated by "table" tags), farm2table places it in a csv file. By default, the first table on the page ends up in table1.csv, the second ends up in table2.csv, and so on. You can change the naming system if you wish, of course.

## Examples
The usefulness of this library becomes apparent very quickly with just a few examples:

First, import farm2table and all its internal classes:

```Python
from farm2table import *
```

Choose a url you want to extract tables from. 
A good example is https://coinmarketcap.com/exchanges/volume/24-hour/ which lists Bitcoin exchanges by volume. 

```Python
url = "https://coinmarketcap.com/exchanges/volume/24-hour/"
```

Convert the url to a Page object and call get_tables:

```Python
page = Page(url)
tables = page.get_tables()
```

To save all the tables, simply call save_tables:

```Python
page.save_tables(tables)
```

Now look in your directory. You will see a csv file called "table1.csv" that contains the data in the url.

