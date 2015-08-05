__author__ = 'eugene'

import scraperwiki
from lxml import etree
import lxml.html
import string
from datetime import datetime
import csv
import urllib
import re
import json

def getJobCount(url):
    
    response = urllib.urlopen(url)
    #print response.read()
    j = json.loads(response.read())
    return j['totalCount']



urls = [
      ['BA all', 'https://api.seek.com.au/v2/jobs/search?keywords=.net&graduateSearch=false&location=1002&isAreaUnspecified=false&salaryRange=100000-999999&salaryType=annual&dateRange=31']
    , ['BA contract', 'https://api.seek.com.au/v2/jobs/search?keywords=.net&graduateSearch=false&location=1002&isAreaUnspecified=false&salaryRange=100000-999999&salaryType=annual&dateRange=31&worktype=244']
    , ['BA perm', 'https://api.seek.com.au/v2/jobs/search?keywords=.net&graduateSearch=false&location=1002&isAreaUnspecified=false&salaryRange=100000-999999&salaryType=annual&dateRange=31&worktype=242']
    , ['.net all', 'https://api.seek.com.au/v2/jobs/search?keywords=.net&graduateSearch=false&location=1002&isAreaUnspecified=false&salaryRange=100000-999999&salaryType=annual&dateRange=31']
    , ['.net contract', 'https://api.seek.com.au/v2/jobs/search?keywords=.net&graduateSearch=false&location=1002&isAreaUnspecified=false&salaryRange=100000-999999&salaryType=annual&dateRange=31&worktype=244']
    , ['.net perm', 'https://api.seek.com.au/v2/jobs/search?keywords=.net&graduateSearch=false&location=1002&isAreaUnspecified=false&salaryRange=100000-999999&salaryType=annual&dateRange=31&worktype=242']
    , ['java all', 'https://api.seek.com.au/v2/jobs/search?keywords=java&hirerId=&hirerGroup=&page=1&classification=6281&subclassification=&graduateSearch=false&location=1002&salaryRange=100000-999999&salaryType=annual&dateRange=31']
    , ['java contract', 'https://api.seek.com.au/v2/jobs/search?keywords=java&hirerId=&hirerGroup=&page=1&classification=6281&subclassification=&graduateSearch=false&location=1002&nation=&area=&isAreaUnspecified=false&worktype=244&salaryRange=100000-999999&salaryType=annual&dateRange=31']
    , ['java perm', 'https://api.seek.com.au/v2/jobs/search?keywords=java&hirerId=&hirerGroup=&page=1&classification=6281&subclassification=&graduateSearch=false&location=1002&nation=&area=&isAreaUnspecified=false&worktype=242&salaryRange=100000-999999&salaryType=annual&dateRange=31']
]

extractedOn = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

for url in urls:

    search = url[0]
    cnt = getJobCount(url[1])

    print search
    print cnt

    # Save found data
    scraperwiki.sqlite.save(unique_keys=['extracted_on','search'], data={
        "extracted_on": extractedOn,
        "search": suburb,
	"count": cnt
        })
