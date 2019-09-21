#!/usr/bin/python

import datetime
import os
import sys

if ( len( sys.argv ) == 2 ):
        fname = sys.argv[ 1 ]
else:
	fname = 'cs2k.csv'

print 'Fname:', fname 
print 'Fname w/o suffix:', os.path.splitext( fname )[0] 
opdirname = os.path.splitext( fname )[0] 

x = datetime.datetime.now()

print(x.year)
print( x.strftime( '%Y_%m_%d_%H_%M' ) )
print 'OP Dirname:', opdirname 
opdirname = opdirname + '_' + x.strftime( '%Y_%m_%d_%H_%M' ) 
print 'OP Dirname:', opdirname 
