#!/usr/bin/python
import re
import urllib
import sys
site  = "http://finance.yahoo.com/d/quotes.csv?s="
sym   = sys.argv[1]
h     = urllib.urlopen(site + sym + "&f=shgl1")
j     = h.read()
h.close()
k     = re.findall('(\w+)",(\d+.\d\d),(\d+.\d\d),(\d+.\d\d)',j)
stock = k[0][0]
hi    = float(k[0][1])
lo    = float(k[0][2])
last  = float(k[0][3])
z     = (last-lo)/(hi-lo)
def main():
  if z >= 0.5:
    print "%s is trading in the top half of it's range" % stock
  else:
    print "%s is trading in the bottom half of it's range" % stock
if __name__ == '__main__':
  main()
