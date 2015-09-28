__author__ = 'Pein'

import urllib.request
import os
import re

def open_url(url):
    response = urllib.request.urlopen(url)
    return response.read()

def find_image(data):
    pattern = b'<img src="(.*?\.(png|jpg))" class="external" />'
    img_address = re.findall(pattern, data)
    return img_address

def save_image(img_address, filename):
    for address in img_address:
        image = open_url(address[0].decode('UTF-8'))
        with open(filename, 'wb') as file:
            file.write(image)
            file.close()

if __name__ == '__main__':
    url = 'http://www.appletuan.com'

    dailyPriceURL = 'http://www.appletuan.com/go/dailyprice'
    data = open_url(dailyPriceURL)

    dailyPriceFile = open('dailyPrice.txt', 'wb')

    pattern = b'<a class="rabel topic" href="(/t/\d*)">(.*\s)</a>'

    titles = re.findall(pattern, data)

    for title in titles:
        tempURL = url.encode(encoding='UTF-8') + title[0]

        tempData = open_url(tempURL.decode('ASCII'))
        addresses = find_image(tempData)
        for address in addresses:
            dailyPriceFile.write(address[0] + '\n'.encode('utf-8'))

        # save_image(addresses, title[1])
        dailyPriceFile.write(tempURL + '\n'.encode('utf-8'))
        dailyPriceFile.write(title[1] + '\n'.encode('utf-8'))


    dailyPriceFile.close()

