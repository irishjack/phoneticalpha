#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

if len(sys.argv) < 2:
	print "[-] Nothing to do, please provide the password or string: python script.py myPa$$w0rd"
	sys.exit()

d = {"a":"alpha","b":"bravo","c":"charlie","d":"delta","e":"echo","f":"foxtrot","g":"golf","h":"hotel","i":"india","j":"juliett","k":"kilo","l":"lima","m":"mike","n":"november","o":"oscar","p":"papa","q":"quebec","r":"romeo","s":"sierra","t":"tango","u":"uniform","v":"victor","w":"whiskey","x":"x-ray","y":"yankee","z":"zulu","-":"dash","0":"Zero", "1":"One", "2":"Two", "3":"Three", "4":"Four", "5":"Fife", "6":"Six", "7":"Seven", "8":"Eight", "9":"Niner", "/":"Slash", ":":"Colon", "+":"Plus", ".":"Dot"}

print("[*] Your password/string of length:%d can be read as follows:\n" % (len(sys.argv[1])))
for char in sys.argv[1]:
	if char.lower() in d:
		if char.lower() == char:
			print d[char]
		else:
			print d[char.lower()].upper()
	else:
		print char 

