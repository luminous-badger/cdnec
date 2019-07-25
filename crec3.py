#!/usr/bin/python

# Create test cases for CDsuffnec with 2 - 11 X columns
# From: https://stackoverflow.com/questions/24108417/simple-way-of-creating-a-2d-array-with-random-numbers-python
# JM Wed 24 Jul 10:18:41 BST 2019

import csv
import random
import numpy as np

Xcols = [ 'header', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven' ]

lines = 11
cols  = 11

rqop = np.random.random( (lines, cols) )

sepxxx=','

print( sepxxx.join(Xcols),'\n\n' )

print( 'L:', len( rqop) )

def prfile( cols ):
	fname = str( Xcols[ cols ] ) + '.csv'
	print 'Fname:', fname
	# Change wb to w for Python3
	with open( fname, 'wb' ) as myfile:
		wr = csv.writer( myfile )
		hdrlist = []
		# Add number of headers as reqd, plus four Y cols.
		for hdr in range( 0, cols+1 ):
			print Xcols[ hdr ],
			hdrlist.append( Xcols[ hdr ] )
		print	
		hdrlist.append(  'Y1' )
		hdrlist.append(  'Y2' )
		hdrlist.append(  'Y3' )
		hdrlist.append(  'Y4' )
		wr.writerow( hdrlist )
		linelist = []
		# write defined number of lines to CSV file.
		for lines in range( 1, 12 ):
			print  lines, 
			linelist.append( lines )
			for clm in range( 0, cols ):
				print  '{:0.2f}'.format( random.random() ),
				linelist.append( '{:0.2f}'.format( random.random() ) )
			for Y in range( 1,5 ):
				# Append four Y cols.
				linelist.append( '{:0.2f}'.format( random.random() ) )
			print	
			wr.writerow( linelist )
			linelist = []
		print ' =-=-=-=-'	

for a in range( 2, 12 ):
	prfile( a )
	#print	a

