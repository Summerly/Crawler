__author__ = 'Pein'

import urllib.request
import os
import re

url = 'http://www.appletuan.com/'

dailyPriceURL = 'http://www.appletuan.com/go/dailyprice'

data = urllib.request.urlopen(dailyPriceURL).read()

dailyPriceFile = open('dailyPrice.txt', 'wb')

dailyPriceFile.write(data)

dailyPriceFile.close()