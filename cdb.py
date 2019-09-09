#!/usr/bin/python

#works !

#import matplotlib.pyplot as plt
#from scipy.stats import norm, f
## Gives: Internal Server Error

# http://www.ruralvisits.com/cgi-bin/cdb.py?fname=ten.csv 
# This is the URL genereated to call cdb.py

from datetime import datetime
import itertools
import csv
import sys
import os
import cgi

form = cgi.FieldStorage()

print( 'Content-type: text/html\n' )
print( '<TITLE>QCA</TITLE> ' )
print( '<br>' )
print( '<br>' )
print( '<h1>Fuzzy Set Goodness of Fit</h1>' )
print( '<br>' )
html = """
<P>Processing %s </P>
"""

fmsg = '<p> Filename: NOT FOUND<p>'
if not 'fname' in form:
	print( fmsg )
else:
	print(html % ('Filename: %s ' % form['fname'].value))

ymsg = '<p> Y Col SET to 1 <p>'
if not 'Ycol' in form:
	print( ymsg )
else:
	print(html % ('Ycol: %s ' % form['Ycol'].value))

varlist = [ 1,2,3,4,5,6,7 ]

msg = '<p> msg: ' + str( varlist[1] ) + ' end msg</p>'

print( msg )
print( '<p>Version: N</p>' )

