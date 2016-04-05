# farm2table
Seamlessly extract HTML tables from websites and convert them to CSV with Python.

## Installation

It (will) be on PyPI so you can install farm2table with:
```
pip install farm2table
```

## Explanation
farm2table arose out of a need to extract HTML tables from websites without coding up a scraper each time. With this library, you can automatically extract each table from a given website and save them to csv files without much trouble. 

For every table on a given website (delineated by "table" tags), farm2table takes each entry and places it in a csv file. By default, the first table on the page ends up in table1.csv, the second ends up in table2.csv, and so on. You can change this if you wish, of course.

## Examples
The usefulness of this library becomes apparent very quickly with just a few examples: