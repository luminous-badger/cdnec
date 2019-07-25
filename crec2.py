#!/usr/bin/python

# Create test cases for CDsuffnec with 2 - 11 X columns
# From: https://stackoverflow.com/questions/24108417/simple-way-of-creating-a-2d-array-with-random-numbers-python
# JM Wed 24 Jul 10:18:41 BST 2019
# Didn't need 2D list. Used print and func call instead.
# Works. later verson with file write in crec3.
# JM Thu 25 Jul 2019 21:34:58 BST

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
	for hdr in range( 0, cols+1 ):
		print Xcols[ hdr ],
	print	
	for lines in range( 1, 4 ):
		print  lines, 
		for clm in range( 0, cols ):
			print  '{:0.2f}'.format( random.random() ),
		print	
	print ' =-=-=-=-'	

for a in range( 2, 12 ):
	prfile( a )
	#print	a

'''
for n in range( 1,12):
	print 'N:', n ,
	print ' --------'	
	print	
'''	
