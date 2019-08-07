#!/usr/bin/python

#works !

#import matplotlib.pyplot as plt
#from scipy.stats import norm, f
## Gives: Internal Server Error
from datetime import datetime
import itertools
import csv
import sys
import os

print( 'Content-type: text/html\n' )
print( '<TITLE>QCA</TITLE> ' )
print( '<p>Fuzzy Set Goodness of Fit</p>' )
print( '<p> CSV xMAT ITER xSCIPY DATE VAR Fuzzy Set Goodness of Fit</p>' )

varlist = [ 1,2,3,4,5,6,7 ]

