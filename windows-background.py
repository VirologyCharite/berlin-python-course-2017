import ctypes
import os
import requests,os,subprocess,bs4,urlparse

SPI_SETDESKWALLPAPER = 20

def get_potd():
    potd_page = 'http://photography.nationalgeographic.com/photography/photo-of-the-day'
    #Try five times and then quit
    for i in range(5):
        try:
            r = requests.get(potd_page)
            if r.status_code == 200:
                soup = bs4.BeautifulSoup(r.content)
                div = soup.find('div', {'class': 'primary_photo'})
                url = div.img['src']
                name = os.path.basename(urlparse.urlparse(url).path)
                if 'http' not in url:
                    url = 'http:%s' % url
                content = requests.get(url).content
                open('national-geographic.jpg', 'wb').write(content)
                return name
            else:
                print 'Failed with http status %s, trying again. . .' % r.status_code
        except Exception as inst:
            print 'Failed with exception: %s, trying again. . .' % inst 
    return None           


ctypes.windll.user32.SystemParametersInfoW(
    SPI_SETDESKWALLPAPER, 0, , 3) 
