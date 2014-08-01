#This web scraper pulls information from findthemissing.org
#We will be pulling the following: the link to the case number,picture, name, address.

import requests
import lxml.html

#possible storage = file system
class NamUSGrab:
    def __init__(self):
        self.cases = []
    
    def pageGrab(self,url_query):
        base_query = url_query
        r = requests.get(url_query)
        count = 1
        while r.status_code == 200:

            html = lxml.html.fromstring(r.text)
            
            self.cases.append([]
            url_query = url_query.replace(str(count),str(count+1))
            count += 1
            r = requests.get(url_query)

        return cases
https://www.findthemissing.org/en/cases/search/thumbnail?direction=asc&order=cases.DateLKA&page=1
