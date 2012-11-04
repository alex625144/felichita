#! /usr/bin/env python3
f=None
f=open('/home/alex/ux.csv', 'r', encoding='cp1251')
d=None
d=open('/home/alex/ux2.csv', 'w', encoding='cp1251')

while True:
	line=f.readline()	
	if not line:break
	
	if(line.find(";A;")>1): 
		newline=line.replace("  ", ";")
		d.writelines(newline)
	
	
f.close()
d.close()
