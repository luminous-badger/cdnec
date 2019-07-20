#!/usr/bin/python

import itertools


def proc_cons(XvalList=[]):
    for n in range(len(XvalList)):

        if (len(XvalList[n]) == 1):
            print 'Call ONE'
            #proc_cons1(XvalList[n])


varlist = [1, 2, 3, 4]

print 'VList:', varlist

for Xindex in range(1, len(varlist) + 1):
    XvalList = list(itertools.combinations(varlist, Xindex))
    print 'List:', XvalList, 'LX:', len(XvalList)
    proc_cons( XvalList )
