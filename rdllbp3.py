#!/usr/bin/python3

# Read in file and add to dictionary. Python 3 version.
# No longer uses indvidual add to list. Adds direct to dictionary. Improvement !
# JM Mon 26 Aug 12:37:40 BST 2019

import csv
import sys
import os

if ( len( sys.argv ) == 1 ):
	fname = 'cs2k.csv'
	Yval = 1
elif ( len( sys.argv ) == 2 ):
	fname = sys.argv[ 1 ]
	Yval = 1
elif ( len( sys.argv ) == 3 ):
	fname = sys.argv[ 1 ]
	Yval = int( sys.argv[ 2 ] )
else:
	fname = 'cs2k.csv'
	Yval = 1

if ( Yval > 4 ):
	# Can't allow Y to be more than four. Only four Y vals allowed.
	Yval = 1

X0list = []
X1list = []
X2list = []
X3list = []
X4list = []
X5list = []
X6list = []
X7list = []
X8list = []
X9list = []
X10list = []
X11list = []
YNlist  = []

column_dict = {
1 : X1list ,
2 : X2list ,
3 : X3list ,
4 : X4list ,
5 : X5list ,
6 : X6list ,
7 : X7list ,
8 : X8list ,
9 : X9list ,
10 : X10list ,
11 : X11list ,
12 : YNlist
}

def read_file():
	
	with open( fname, 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			linelist = list( row )			
			linel = len( linelist )
			CDYval = linel - 5 + Yval 
			print( 'LL:', linel, ' CDY:', CDYval )
			# Use for loop and append. Don't need to add to each list by name.
			# Convert to float as read in as string.
			# Last four cols in input file are the Y vals.
			for Xlocal in range ( 1, linel - 4 ):
				print( 'X:', Xlocal, linelist[ Xlocal ] )
				#print( 'TY:', Xlocal, type( linelist[ Xlocal ] ) )
				try:
					column_dict[ Xlocal ].append( float ( linelist[ Xlocal ] ) )
				except:
					print( 'CD Err:', linelist[ Xlocal ] )
			try:
				column_dict[ 12 ].append( float ( linelist[ CDYval ] ) )
			except:
				print( 'CD YErr:', linelist[ Xlocal ] )

# End #####################

print( 'Start' )
read_file()
print( 'Yval:', Yval )
print( 'YNlist:', YNlist )
print( 'CD:', column_dict )

