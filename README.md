# goodx_reports
## Scripts for dealing with GoodX reports
### Repository of scripts used for data handling for the GoodX system for use at the University of Pretoria School of Dentistry
#### Yasin's Log 02/03/2020
##### file_handler.py, language - python3
1. You created a function which compiles GoodX CSV reports from admindaily and edudaily to a single admin and edu file.
2. This program defines a location where the CSVs are stored. By default it is a subdirectory called 'raw_data'
3. This program looks for .csv files in this subdirectory.
4. It then adds those with admin in the name to admin_list and those - with edu in the name to edu_list
5. It is possible to break this file sorting function by being an idiot. Don't be an idiot for your own sake.
6. You decided to use parquet file with gzip compression for a few reasons:
     * The data is too big to evaluate in Excel/Calc anyway, so no point even trying it
     * Feather file format handles indices by making it a column. This may create multiple index columns in future exports
     * The compressed file is a convenient size (significantly smaller than csv, xlsx, and ftr)
7. You export these files to a subdirectory called gzip.
7. You explicitly cast telephone numbers to string and made null values = 'None' to avoid future errors
8. You used `low_memory=False` during imports - helped solve your issues with null values
9. Null values are a pain!
10. This may be silly but your new favourite pandas trick is:
    * `data[~data['Column'].random_function()]`: the inclusion of the tilde results in the inverse, handy!
11. You used a for loop. You tried list comprehension but there appeared to be memory issues. You got around this by:
    * Using concatenation instead of creating new variables
    * Clearing the memory with python's `del` statement
12. You want to serve up some of this data on a Rasperry Pi so you need to be conservative with resources, luckily you have multiple other options to do this heavy lifting.
13. Holding multiple dataframes in memory simultaneously makes this program crash - using list comprehension results in a 'Killed' error. Read the following links when you have time again:
    * [A question answered on Stackoverflow about this error](https://stackoverflow.com/questions/19189522/what-does-killed-mean "Python - What does killed mean?")
    * [A page about the 'OOM killer'](https://lwn.net/Articles/761118/)
