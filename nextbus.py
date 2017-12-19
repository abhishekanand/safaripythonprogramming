# nextbus.py

import sys

print('Command Options:', sys.argv)
# holds Argument that is passed while using script in command line
raise SystemExit(0)
# To exit the pra


import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14787&route=22')
data = u.read()
print(data)

from xml.etree.ElementTree import XML
doc = XML(data)
print(doc)

for pt in doc.findall('.//pt'):
    print(pt.text)

print("Done")