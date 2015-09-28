__author__ = 'Pein'

import urllib.request
import os
import re

url = 'http://www.appletuan.com/'

dailyPriceURL = 'http://www.appletuan.com/go/dailyprice'

data = urllib.request.urlopen(dailyPriceURL).read()

dailyPriceFile = open('dailyPrice.txt', 'wb')

pattern = b'<a class="rabel topic" href="(/t/\d*)">(.*\s)</a>'

titles = re.findall(pattern, data)

for title in titles:
    dailyPriceFile.write(url.encode(encoding='UTF-8') + title[0])
    dailyPriceFile.write(title[1])

dailyPriceFile.close()


