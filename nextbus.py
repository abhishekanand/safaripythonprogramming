# nextbus.py

import sys

if len(sys.argv) !=3:
    raise SystemExit('Usage: nextbus.py route stopid')
route = sys.argv[1]
stopid = sys.argv[2]


import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop={}&route={}'.format(stopid,route))
data = u.read()
#print(data)

from xml.etree.ElementTree import XML
doc = XML(data)
#print(doc)

for pt in doc.findall('.//pt'):
    print(pt.text)

print("Done")