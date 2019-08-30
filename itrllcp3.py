#!/usr/bin/python3

# Read in file and add to dictionary. Python 3 version.
# No longer uses indvidual add to list. Adds direct to dictionary. Improvement !
# JM Mon 26 Aug 12:37:40 BST 2019
# Splits up combination list into indivdual lists and then processes the in one proc.
# No need for multiple procs.
# JM Fri 30 Aug 16:17:13 BST 2019

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
    # xlist not getting enough values. move it somewhere ?
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
        xlist_plot = []
        fnamecs = 'X' 
        fnameds = 'DX' 
        pltitlecs = 'Plot of Y' + str( Yval ) + ' & Minimum of X'
        pltitleds = 'Plot of Z(Y' + str( Yval ) + ') & Z( Minimum of X'
        for xv in( XvalListn ):
            #print( 'LCD:', LCD, ' CDxv:', column_dict[ xv ][LCD], end ='\n' )
            #print('XVCD:',xv,  column_dict[ xv ] )
            numrl.append(  column_dict[ xv ][LCD] )    
            denrl.append(  column_dict[ xv ][LCD] )    
            fnamecs = fnamecs + str(xv)
            fnameds = fnameds + str(xv)
            pltitlecs = pltitlecs + str(xv) 
            pltitleds = pltitleds + str(xv) 
        numrl.append(  column_dict[ 12 ][LCD] )    
        # numerator is min of row & Y val
        # denominator is just min of row.
        print( 'NUMRL:', numrl, min( numrl ) )    
        print( 'DENRL:', denrl, min( denrl ) )    
        CsuffNum += min(numrl)
        CsuffDen += min(denrl)
        xlist_plot.append( min(denrl) )
    print( 'CsuffNum:', CsuffNum )
    print( 'CsuffDen:', CsuffDen )
    print()
    if ( CsuffDen != 0 ):
        Csuff = CsuffNum / CsuffDen
        print( 'Csuff:', Csuff  )
    fnamecs = fnamecs + 'Y' + str(Yval) + '.png'
    fnameds = fnameds + 'Y' + str(Yval) + '.png'
    pltitlecs = pltitlecs + '; Csuff = ' + str( Csuff )
    pltitleds = pltitleds + ' )'
    print( 'Fnamecs:', fnamecs )
    print( 'Fnameds:', fnameds )
    print( 'Pltitlecs:', pltitlecs )
    print( 'Pltitleds:', pltitleds )
    print( 'Xlist_plot:', xlist_plot )
    # Need 2 pltitles, 2 fname, graph plot and Dsuff proc.
    #plot_graph( xlist_plot, column_dict[ CDYval ], pltitlecs, Csuffcs, fnamecs )
    #proc_Dsuff( xlist_plot, column_dict[ CDYval ], pltitleds, Csuff, fnameds )



# BBBBBBBBBBBBBBB

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
        proc_cons4b( xvv )
        #proc_cons( XvalList)
