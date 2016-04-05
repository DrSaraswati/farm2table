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
The usefulness of this library becomes apparent very quickly with just a few examples. I made an example script called "example.py" that you can find in the repo if you want something out of the box. 

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

Now look in your directory. You will see a csv file called "table1.csv" that contains the data in the url, exactly as it appears on their website. This is about 650 rows of data.

Sometimes, certain websites will use <table> tags to structure the layout of their page, and not to display data as you might expect. Websites shouldn't do that, but some still do. If you want to ignore any of these "table fragments" that are a result of HTML tables being used for layout purposes, simply add an extra command to save_tables:

```Python
page.save_tables(tables, ignore_small=True)
```

This new argument causes the code to ignore any table with 5 entries or fewer. As a byproduct, most table fragments and layout elements are ignored. It's not perfect, but it's pretty good for now. 

