__author__ = 'Pein'

import urllib.request
import urllib
import os

eBook = '电子书'

eBook = urllib.parse.quote(eBook)

# url = "http://www.amazon.cn"

kindleURL = "http://www.amazon.cn/Kindle%s/b/ref=sa_menu_firetab_l2_116169071?ie=UTF8&node=116169071" %(eBook)

# usKindleURL = "http://www.amazon.com/Kindle-eBooks/b?ie=UTF8&node=154606011"

print(kindleURL)

data = urllib.request.urlopen(kindleURL)

file = open('test.txt', 'wb')

file.write(data.read())

file.close()
