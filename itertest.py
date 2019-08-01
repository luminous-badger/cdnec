#!/usr/bin/python3

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

# Add 6 to get correct offset. Y1 is column 7, etc. CD is short for column_dict. 
CDYval = Yval + 6

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
    print( 'Reading:', fname )    
    with open( fname, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            linelist = list( row )            
            #for Xlocal in range ( 1, XvalMax ):
            try:
                X0list.append( linelist[ 0 ] )
                #print( 'Xlist:', Xlist )
            except:
                #print( 'XErr:',  linelist[ 0 ] )
                pass
            try:
                X1list.append( float( linelist[ 1 ] ) )
                #print( 'Xlist: 1', linelist )
            except:
                #print( 'XErr:1' ,  linelist[ 1 ] )
                pass
            try:
                X2list.append( float( linelist[ 2 ] ) )
                #print 'Xlist:', Xlist
            except:
                #print( 'XErr 2:',  linelist[ 2 ] )
                pass
            try:
                X3list.append( float( linelist[ 3 ] ) )
                #print 'Xlist:', Xlist
            except:
                #print 'XErr:',  linelist[ 3 ]
                pass
            try:
                X4list.append( float( linelist[ 4 ] ) )
                #print 'Xlist:', Xlist
            except:
                #print 'XErr:',  linelist[ 4 ]
                pass
            try:
                X5list.append( float( linelist[ 5 ] ) )
                #print 'Xlist:', Xlist
            except:
                #print 'XErr:',  linelist[ 5 ]
                pass
            try:
                X6list.append( float( linelist[ 6 ] ) )
                #print 'Xlist:', Xlist
            except:
                #print 'XErr:',  linelist[ 6 ]
                pass            
            try:
                YNlist.append( float( linelist[ CDYval ] ) )
            except:
                #print 'Yerr:', linelist[ CDYval ]
                pass

#************** Processing ************** 


def proc_cons2(XvalListn=[]):
    print( 'P2LenXV:', len(XvalList) )
    #print( '\nLen col dict:', len( column_dict[ 1 ] ), '\n\n' )
    x1,x2 = XvalListn
    xlist_plot = []
    Csuff    = 0.0 
    CsuffNum = 0.0 # Csuff Numerator
    CsuffDen = 0.0 # Csuff Denominator
    fname = 'X' + str( x1 ) + str( x2 ) + 'Y' + str( Yval ) + '.png'
    for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
        print( 'LCD:', LCD )
        CsuffNum +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ CDYval ][ LCD ] ) 
        CsuffDen +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ] ) 
        xlist_plot.append( min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ] ) )

    if ( CsuffDen != 0 ):
        Csuff = CsuffNum / CsuffDen
'''
    for LCD in range( 0, len( column_dict[ 1 ] ), 1 ):
        print( 'LCD:', LCD )
for LCD in range( 0, len( column_dict[ x1 ] ), 1 ):
CsuffNum +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ], column_dict[ CDYval ][ LCD ] )
CsuffDen +=  min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ] )
xlist_plot.append( min( column_dict[ x1 ][ LCD ], column_dict[ x2 ][ LCD ] ) )
'''

def proc_cons(XvalList=[]):
    for n in range(len(XvalList)):

        if (len(XvalList[n]) == 1):
            print( n,' Call ONE' )
            #print( 'XVal', XvalList[n] )
            #proc_cons1(XvalList[n])
        elif (len(XvalList[n]) == 2):
            print( 'LGT Two:' )
            print( 'XValGT 2:', XvalList[n] )
            proc_cons2(  XvalList[ n ] )
####################### main #######################

print( 'Calling RF:' )
read_file()

varlist = [1, 2, 3, 4]

print( 'VList:', varlist )

for Xindex in range(1, len(varlist) + 1):
    XvalList = list(itertools.combinations(varlist, Xindex))
    #print( 'Ind:',Xindex, 'List:', XvalList, 'LX:', len(XvalList) )
    proc_cons( XvalList )
