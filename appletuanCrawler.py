__author__ = 'Pein'

import urllib.request
import os
import re

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
    response = urllib.request.urlopen(req)
    return response.read()

def find_image(data):
    pattern = b'<img src="(.*?\.(png|jpg))" class="external" />'
    img_address = re.findall(pattern, data)
    return img_address

def save_image(img_address, filename):
    image = open_url(img_address)
    filename = img_address.split('/')[-1]
    print(filename)
    with open(filename, 'wb') as file:
        file.write(image)
        file.close()

def download_images(url, titles):
    dirname = 'downloads'

    if not os.path.exists(dirname):
        os.mkdir(dirname)

    if os.path.dirname(os.getcwd()) != dirname:
        os.chdir(dirname)

    for title in titles:
        tempURL = url.encode(encoding='UTF-8') + title[0]

        tempData = open_url(tempURL.decode('ASCII'))
        addresses = find_image(tempData)
        for address in addresses:
            save_image(address[0].decode('utf-8'), title[1])

if __name__ == '__main__':
    url = 'http://www.appletuan.com'

    dailyPriceURL = 'http://www.appletuan.com/go/dailyprice'
    data = open_url(dailyPriceURL)
    pattern = b'<a class="rabel topic" href="(/t/\d*)">(.*\s)</a>'
    titles = re.findall(pattern, data)

    download_images(url, titles)







