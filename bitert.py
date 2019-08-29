#!/usr/bin/python3

import itertools


def proc_cons(XvalList=[]):
    for n in range(len(XvalList)):

        #print( 'L:', len( XvalList ) )
        print( XvalList )
        '''
        if (len(XvalList[n]) == 1):
            print( 'Call ONE' )
            #proc_cons1(XvalList[n])
        elif ( len( XvalList[ n ] ) == 2 ):
            #print( 'Call TWO' )
            print( 'L:', len( XvalList ) )
            print( 'XV:', XvalList[ 0 ], XvalList[ 1 ] )
        '''

#varlist = [1, 2, 3, 4]
varlist = list( range(1,5) )

print( 'VList:', varlist )

for Xindex in range(1, len(varlist) + 1):
    XvalList = list(itertools.combinations(varlist, Xindex))
    for xvv in( XvalList ):
        print( 'XVV:', xvv )
    #print( 'List:', XvalList, 'LX:', len(XvalList) )
    #print( len(XvalList) )
    #proc_cons( XvalList )
