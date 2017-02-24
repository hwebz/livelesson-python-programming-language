import sys

if len(sys.argv) != 3:
	raise SystemExit('Usage: nextbus.py route stopid')

route = sys.argv[1] # 		22 			6
stopid = sys.argv[2] #	 	14791 		5037

# print('Command options:', sys.argv)
# raise SystemExit(0)
import urllib.request

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stop={}'.format(route,stopid))
data = u.read()

from xml.etree.ElementTree import XML
doc = XML(data)

for pt in doc.findall('.//pt'):
	print(pt.text)