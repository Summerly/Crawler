__author__ = 'Pein'

import urllib.request
import urllib
import os
import re

eBook = '电子书'
eBook = urllib.parse.quote(eBook)

# url = "http://www.amazon.cn"
kindleURL = "http://www.amazon.cn/Kindle%s/b/ref=sa_menu_firetab_l2_116169071?ie=UTF8&node=116169071" %(eBook)
# usKindleURL = "http://www.amazon.com/Kindle-eBooks/b?ie=UTF8&node=154606011"

testURL = "http://www.amazon.cn/gp/product/B00KYEFUZC?colid=2ZWLDZCLM39H6&coliid=I1OIMJ4248SEQ6&ref_=wl_it_dp_o_pC_nS_ttl"

# data = urllib.request.urlopen(testURL)

# file = open('test.txt', 'wb')
#
# file.write(data.read())
#
# file.close()

readFile = open('test.txt', 'rb')

      # <b class="priceLarge" >
      #   ￥ 56.61
      # </b>

pattern = b'<b class="priceLarge" >(\S*)</b>'

price = re.findall(pattern, readFile.read())

outFile = open('out.txt', 'w')
# outFile.write()

print(price)

readFile.close()
outFile.close()


