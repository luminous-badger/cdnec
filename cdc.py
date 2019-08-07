#!/usr/bin/python

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
print( '<p> CSV ITER DATE VAR X&Y FORM FNAME BTTN</p>' )

print( '<p>Enter a file name</p> ' )
print( '<br>' )
print( '<form action="./cgi-bin/cdb.py" > ' )
print( '  Select a file: <input type = "file" name = "myfile" ><br><br> ' )
print( '  <input type = "submit" > ' )
print( '</form> ' )
print( '<br>' )

print( '<p>Choose number of X-Columns</p>' )
print( '<form>' )
print( '<input type="radio" name="xcol" value="2" > 2<br>' )
print( '  <input type="radio" name="xcol" value="3" > 3<br> ' )
print( '  <input type="radio" name="xcol" value="4" > 4<br> ' )
print( '  <input type="radio" name="xcol" value="5" > 5<br> ' )
print( '  <input type="radio" name="xcol" value="6" > 6<br> ' )
print( '  <input type="radio" name="xcol" value="7" > 7<br> ' )
print( '  <input type="radio" name="xcol" value="8" > 8<br> ' )
print( '  <input type="radio" name="xcol" value="9" > 9<br> ' )
print( '  <input type="radio" name="xcol" value="10" > 10<br> ' )
print( '  <input type="radio" name="xcol" value="11" > 11<br> ' )
print( '</form>' )
print( '<br>' )

print( ' <p>Choose Y-Column</p> ' )
print( '  <form> ' )
print( '   <input type="radio" name="Ycol" value="1" > Y1<br> ' )
print( '   <input type="radio" name="Ycol" value="2" > Y2<br> ' )
print( '   <input type="radio" name="Ycol" value="3" > Y3<br> ' )
print( '   <input type="radio" name="Ycol" value="4" > Y4<br> ' )
print( ' </form> ' )


print( '<p> </p>' )
varlist = [ 1,2,3,4,5,6,7 ]

