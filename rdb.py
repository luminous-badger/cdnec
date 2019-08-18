#!/usr/bin/python

# Test read in of file of any width.
# JM Sat 17 Aug 2019 19:41:34 BST

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
CDYval = Yval

X0list = []
X1list = []
X2list = []
X3list = []
X4list = []
X5list = []
X6list = []
YNlist = []

column_dict = {
1 : X1list ,
2 : X2list ,
3 : X3list ,
4 : X4list ,
5 : X5list ,
6 : X6list ,
CDYval  : YNlist
}

def read_file():
	
	with open( fname, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			linelist = list( row )			
			print 'Linelist:', linelist
			LenLL = len( linelist )
			print 'Len:', LenLL

			# Depends of length of input line. There are four Y vals at rightmost of input file. Need length of input file.
			# CDYVAL Must be declared before this function --=--=--=--=--
			# Also need to set length of dictionary above to take account of number of input columns. TO DO !!
			# Linelist: ['header', 'one', 'two', 'Y1', 'Y2', 'Y3', 'Y4']     Len: 7
			CDYval = LenLL - 5 + Yval 
			print 'CDYval:', CDYval

			#for Xlocal in range ( 1, XvalMax ):
			try:
				X0list.append( linelist[ 0 ] )
				print 'Xlist:', X0list
			except:
				print 'XErr0:',  linelist[ 0 ]
				pass
			try:
				X1list.append( float( linelist[ 1 ] ) )
				print 'Xlist:', X1list
			except:
				print 'XErr1:',  linelist[ 1 ]
				pass
			try:
				X2list.append( float( linelist[ 2 ] ) )
				print 'Xlist:', X2list
				pass
			except:
				print 'XErr2:',  linelist[ 2 ]
				pass
			try:
				X3list.append( float( linelist[ 3 ] ) )
				print 'Xlist:', X3list
			except:
				print 'XErr3:',  linelist[ 3 ]
				pass
			try:
				X4list.append( float( linelist[ 4 ] ) )
				print 'Xlist:', X4list
			except:
				print 'XErr4:',  linelist[ 4 ]
				pass
			try:
				X5list.append( float( linelist[ 5 ] ) )
				print 'Xlist:', X5list
			except:
				print 'XErr5:',  linelist[ 5 ]
				pass
			try:
				X6list.append( float( linelist[ 6 ] ) )
				print 'Xlist:', X6list
			except:
				print 'XErr6:',  linelist[ 6 ]
				pass			
			try:
				YNlist.append( float( linelist[ CDYval ] ) )
				print 'YNlist:', YNlist 
			except:
				print 'YerrY:', linelist[ CDYval ]
				pass

print 'Start'
read_file()
