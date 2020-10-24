"""
Uses gspread to work with google sheets.

Takes data list from library_scraper module and inputs it into spreadsheet.
"""

import gspread
import time
import library_scraper

gc = gspread.service_account("/Users/jacobsanjuan/Desktop/python_for_programmers/library-database.json")

sh = gc.open("Library Database")

worksheet = sh.worksheet('Delaware')

count_char = 64
for element in library_scraper.headers:
    count_char += 1
    cell = chr(count_char) + '1'
    worksheet.update(cell, element)

count_char = 64
count = 0
row = 2
for element in library_scraper.data:
    count_char += 1
    count += 1
    if count_char > 69:
        count_char = 65
        row += 1
    cell = chr(count_char) + str(row)
    worksheet.update(cell, element)
    time.sleep(2)