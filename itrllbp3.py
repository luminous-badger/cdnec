#!/usr/bin/python3

# Read in file and add to dictionary. Python 3 version.
# No longer uses indvidual add to list. Adds direct to dictionary. Improvement !
# JM Mon 26 Aug 12:37:40 BST 2019

import itertools
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

print( 'F:', fname )

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
	print( 'Reading:', fname )    
	with open( fname, 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			linelist = list( row )			
			linel = len( linelist )
			CDYval = linel - 5 + Yval 
			# NumXcols = line len minus 4 Y cols and 1 header col.
			NumXcols = linel - 5 
			#print( 'LL:', linel, ' CDY:', CDYval )
			# Use for loop and append. Don't need to add to each list by name.
			# Last four cols in input file are the Y vals.
			for Xlocal in range ( 1, linel - 4 ):
				#print( 'X:', Xlocal, linelist[ Xlocal ] )
				try:
					column_dict[ Xlocal ].append( float ( linelist[ Xlocal ] ) )
				except:
					print( 'CD Err:', linelist[ Xlocal ] )
					pass
			try:
				column_dict[ 12 ].append( float ( linelist[ CDYval ] ) )
			except:
				#print( 'CD YErr:', linelist[ Xlocal ] )
				pass
	return NumXcols

#************** Processing ************** 
def proc_cons4b( XvalListn=[]):
    #x1,x2,x3,x4 = XvalListn
    CsuffNum = 0.0 # Csuff Numerator
    CsuffDen = 0.0 # Csuff Denominator
    print( '4BPnLenXV:', len(XvalListn ) )
    print( '4BPnXV:', XvalListn  )
    print( '\nLen col dict:', len( column_dict[ 1 ] ), '\n\n' )
    # LCD shows number of rows in input file.
    for LCD in range( 0, len( column_dict[ 1 ] ), 1 ):
        print( 'Y:',  column_dict[ 12 ][LCD] )
        numrl = []
        denrl = []
        for xv in( XvalListn ):
            print( 'LCD:', LCD, ' CDxv:', column_dict[ xv ][LCD], end ='\n' )
            print('XVCD:',xv,  column_dict[ xv ] )
            numrl.append(  column_dict[ xv ][LCD] )    
            denrl.append(  column_dict[ xv ][LCD] )    
        numrl.append(  column_dict[ 12 ][LCD] )    
        # numerator is min of row & Y val
        # denominator is just min of row.
        print( 'NUMRL:', numrl, min( numrl ) )    
        print( 'DENRL:', denrl, min( denrl ) )    
        CsuffNum += min(numrl)
        CsuffDen += min(denrl)
    print( 'CsuffNum:', CsuffNum )
    print( 'CsuffDen:', CsuffDen )
    print()
# BBBBBBBBBBBBBBB

def proc_cons4a( XvalListn=[]):
    # WRONG should be for LCD then for XV
    x1,x2,x3,x4 = XvalListn
    CsuffNum = 0.0 # Csuff Numerator
    CsuffDen = 0.0 # Csuff Denominator
    print( '4APnLenXV:', len(XvalListn ) )
    print( '4APnXV:', XvalListn  )
    print( '\nLen col dict:', len( column_dict[ 1 ] ), '\n\n' )
    for xv in( XvalListn ):
        print('XVCD:',xv,  column_dict[ xv ] )
        numrl = []
        for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
            #print( 'LCD:', LCD, ' CDxv:', column_dict[ xv ][LCD], end ='\n' )
            numrl.append(  column_dict[ xv ][LCD] )    
        numrl.append(  column_dict[ 12 ][LCD] )    
        print( 'NUMRL:', numrl, min( numrl ) )    
        CsuffNum += min(numrl)
    print()
# AAAAAAAAAAAAAAAAAAA

def proc_cons4( XvalListn=[]):
    x1,x2,x3,x4 = XvalListn
    CsuffNum = 0.0 # Csuff Numerator
    CsuffDen = 0.0 # Csuff Denominator
    print( '4PnLenXV:', len(XvalListn ) )
    print( '4PnXV:', XvalListn  )
    print( '\nLen col dict:', len( column_dict[ 1 ] ), '\n\n' )
    for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
        print( 'LCD:', LCD, ' CDx1:', column_dict[ x1 ][LCD], ' CDx2:', column_dict[ x2 ][LCD], ' CDx3:', column_dict[ x3 ][LCD], ' CDx4:', column_dict[ x4 ][LCD]  )
        CsuffNum +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ], 
        column_dict[ x4 ][ LCD ], column_dict[ 12 ][ LCD ] ) 
        CsuffDen +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ],
        column_dict[ x4 ][ LCD ] ) 
    print()
    print( 'CsuffNum:', CsuffNum )
    print( 'CsuffDen:', CsuffDen )
    '''
    for xv in( XvalListn ):
    	print('XVCD:',xv,  column_dict[ xv ] )
    '''
    print()
	

def proc_cons3(  XvalListn = [ ] ):

	x1,x2,x3 = XvalListn

	xlist_plot = []
	Csuff    = 0.0 
	CsuffNum = 0.0 # Csuff Numerator
	CsuffDen = 0.0 # Csuff Denominator
	fname = 'X' + str( x1 ) + str( x2 ) + str( x3 ) + 'Y' + str( Yval ) + '.png'
	## LCD is the row number in the input file. Corresponds to the entry in column_dict.
	for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
		print( '3LCD:', LCD, ' X1:', x1, ' X2:', x2, ' X3:', x3 )
		print( 'CD1',  column_dict[ x1 ][ LCD ] )
		CsuffNum +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD
		], column_dict[ 12 ][ LCD ] ) 
		CsuffDen +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ] ) 
		xlist_plot.append( min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ x3 ][ LCD ] ) )

# -------------------


def proc_cons2( XvalListn=[]):
    print( 'P2LenXV:', len(XvalList) )
    print( '\nLen col dict:', len( column_dict[ 1 ] ), '\n\n' )
    x1,x2 = XvalListn
    xlist_plot = []
    Csuff    = 0.0 
    CsuffNum = 0.0 # Csuff Numerator
    CsuffDen = 0.0 # Csuff Denominator
    fname = 'X' + str( x1 ) + str( x2 ) + 'Y' + str( Yval ) + '.png'
    for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
        print( 'LCD:', LCD, x1, x2 )
        print( 'CD1:', column_dict[ x1 ][ LCD ] )
        print( 'CD2:', column_dict[ x2 ][ LCD ] )
        print( 'CDY:', column_dict[ 12 ][ LCD ] )
        #CsuffNum +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ 12 ][ LCD ] ) 
        #CsuffDen +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ] ) 
        #xlist_plot.append( min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ] ) )

    if ( CsuffDen != 0 ):
        Csuff = CsuffNum / CsuffDen

    print()	
'''
    for LCD in range( 0, len( column_dict[ 1 ] ), 1 ):
        print( 'LCD:', LCD )
for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
CsuffNum +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ 12 ][ LCD ] )
CsuffDen +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ] )
xlist_plot.append( min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ] ) )
'''

def proc_consb( xvv=[] ):
    print( 'PCB:', xvv )
    proc_cons4b( xvv )

def proc_cons( XvalList=[]):
    for n in range(len(XvalList)):

        if (len(XvalList[n]) == 1):
            print( n,' Call ONE' )
            #print( 'XVal', XvalList[n] )
            #proc_cons1(XvalList[n])
        elif (len(XvalList[n]) == 2):
            print( 'LGT Two:' )
            print( 'XValGT 2:', XvalList[n] )
            #proc_cons2(  XvalList[ n ])
        elif (len(XvalList[n]) == 3):
            print( 'LGT Three:' )
            #proc_cons3(  XvalList[ n ])
        elif (len(XvalList[n]) == 4):
            print( 'LGT Four:' )
            proc_cons4( XvalList[ n ] )
            #proc_cons4a( XvalList[ n ] )
            proc_cons4b( XvalList[ n ] )
####################### main #######################

print( 'Calling RF:' )
NumXcols = read_file()
print( 'Called rf NumXcols:', NumXcols )

varlist = list( range(1, NumXcols + 1 ) )
# NB range goes from start to end-1. Feature !

print( 'VList:', varlist )
print( 'CD12:', column_dict[ 12 ] )

# Need to cater for diff lengths of xval list. Hence 6 procs in orig prog.

for Xindex in range(1, len(varlist) + 1):
    XvalList = list(itertools.combinations(varlist, Xindex))
    print( 'Ind:',Xindex, 'List:', XvalList, 'LX:', len(XvalList) )
    # use for xv in xvallis from bitert to process each item in xvallist separately.
    for xvv in( XvalList ):
        proc_consb( xvv )
        #proc_cons( XvalList)
