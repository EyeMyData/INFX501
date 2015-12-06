# Azure ServiceUpdatesScraper
# !/usr/bin/python
# -*- coding: utf-8 -*-
# sudo pip install requests

# Imports
import requests
import bs4
import html5lib
import csv
import unicodedata
from unicodedata import normalize

# Very important steps for later writing output data to delimited files
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Grab html from Microsoft website
res = requests.get('https://azure.microsoft.com/en-us/updates/')
res.raise_for_status()

# Alternate parsers are available instead of html5lib
AzureSoup = bs4.BeautifulSoup(res.text, 'html5lib')

# Find all the div elements associates with Service Updates, pass them into python object
text1 = AzureSoup.find_all('div', {'class': 'wa-serviceUpdate'})

# Prime txt file for writing, this method destroys any file with same name
csvFile = open('/Users/ryanbrush/Documents/INFX501/output.txt', 'w')

# Manually set the headers for the data output, plus pointing python to second row
csvFile.write('Data_Services$Data_Platforms$Update_Date$Update_Type$Update_Title$Update_Description'
               + '\n')

# Loop thru each div element in text1, extracting relevant text
# Decision to use dollar sign as delimiter, this symbol is rare in this text file
with open('/Users/ryanbrush/Documents/INFX501/output.txt', 'w'):
    for div in text1:
        csvFile.write(div['data-services']
                      + '$' + div['data-platforms'] # 1st Level
                      + '$' + ', '.join(div.span.text.split('>')) # 2nd Level (ie nested in div with 'span' tag)
                      + '$' + div['data-updatetypes'] # 1st Level
                      + '$' + ', '.join(div.a.text.split('>')) # 2nd Level (ie nested in div with 'a' tag)
                      + '$' + ', '.join(div.p.text.split('>')) # 2nd Level (ie nested in div with 'p' tag)
                      + '\n')

# Don't forget to close the txt file
csvFile.close()

