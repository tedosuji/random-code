###########################################################
# CIS 117 Python Programming: Lab #5
#
# The Web and Search
# Application: Topic web crawler
# Description: open a website to browse topics/concepts
#              will take down a topic and add a counter
#              returns # of topics in a list
#
#Dev Env: Windows 10
#Version: Python 3.6.5
#Date: 7/24/18
# 
###########################################################
import urllib
import urllib.request
import re
from urllib.request import urlopen
import ssl

#prompt user for website to check
site = input("Enter full address to search terms: ")

#prompt user for search term separated by commas
search = input("Enter terms to search separated by commas only: ")
listSearch = search.split(',')

#process to scrape xml doc of site
try: #try block to reach site, write HTML to txt
    test = urlopen(site, context=ssl._create_unverified_context())
    fo = open('offline.txt','w')
    fo.write(str(test.read()))
    fo.close() #close file to process

    for item in listSearch: 
        reg = item[1:] #create a regex str to use for simple search
        with open('offline.txt') as fo:
            items = re.findall(r'[a-zA-Z]'+reg, fo.read())
            print("{0} appears {1} times".format(item, len(items)))

    input("Press any key to quit") #wait for readability
except Exception as e: #if error, write and print error to file
    print(str(e))

    '''
	testing one more time for push settings
    '''
