#__author__ = 'User'
#!/usr/bin/env python

#  Author: Nnamdi Offor
#  Date: 5/15/2014
#
#  A simple script to scrape Twitter account information from
# SocialBakers website, and create CSV file with results.
# *************************************** #

import requests
from bs4 import BeautifulSoup

#Choose which account tags to collect from.
tags = ['brands']
int = 0

for tag in tags:
    tag_file = open(tag + '.csv', 'w')
    tags_pages = [2]
    pages = range(1,tags_pages[int])
    for page in pages:
        current_page = requests.get('http://www.socialbakers.com/twitter/group/' + tag + '/page-' + str(page) + '/')
        data = current_page.text
        soup = BeautifulSoup(data)
        table = soup.find_all("table", {"class":"common-table"})[3]

        for tr in table.findAll("tr")[1:]:
            cells = tr.findAll("td")
            rank = cells[0].text.encode("UTF-8").split()
            profile_raw = ' '.join(cells[1].text.encode("UTF-8").split())
            profile = profile_raw.strip().strip(')').replace('(', '')
            followers = cells[3].text.encode("UTF-8").split()
            page_data = "%s, %s, %s \n" % (' '.join(rank), profile, ' '.join(followers))
            tag_file.write(page_data)
    tag_file.close()
    int += 1