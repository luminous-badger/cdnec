#!/usr/bin/python3

'''
See:
https://likegeeks.com/python-gui-examples-tkinter-tutorial/
https://riptutorial.com/tkinter/example/29714/place--
Removed X cols as not needed.
JM Wed 28 Aug 10:45:32 BST 2019
'''

from tkinter import *
from tkinter.ttk import *
import os

csvlist = [ ]

flist = os.listdir( './' )
for f in ( flist ):
    if ( f.endswith( '.csv' ) ):
        csvlist.append( f )
	# Only append csv files for combo box file choice.

rownum = 0
 
def clicked():
	msg = 'Running ' + combofn.get() + ' Y: ' + str( yvar1.get() )
	lblfille.configure(text = msg )
	#print( 'FName:', combofn.get(), ' Ty:', type( combofn.get() ) )
	#print( 'XCols:', comboxc.get() )
	#print( 'Yval1:', yvar1.get() )

window = Tk()
 
window.title("FSGOF")
window.geometry('350x400')
 
lbl = Label(window, text="Fuzzy Set Goodness of Fit")
 
lbl.grid(column=0, row=rownum)
#print('R:', rownum)
rownum += 1
 
lblfilla = Label(window, text="")
 
lblfilla.grid(column=0, row=rownum)
#print('R:', rownum)
rownum += 1
 
lbl2 = Label(window, text="Enter a File Name")
 
lbl2.grid(column=0, row = rownum )
#print('R:', rownum)
rownum += 1

lblfillc = Label(window, text="")
 
lblfillc.grid(column=0, row=rownum)
#print('R:', rownum)
rownum += 1
 
combofn = Combobox(window)
#combofn['values'] = ( 'IndiaResistdata2006.csv', 'cs2k.csv' )
combofn['values'] = csvlist 
combofn.current(0) #set the selected item
combofn.grid(column=0, row = rownum )
#print('R:', rownum)
rownum += 1

lblfillb = Label(window, text="")
 
lblfillb.grid(column=0, row = rownum)
#print('R:', rownum)
rownum += 1
 
lblfillc = Label(window, text="")
 
lblfillc.grid(column=0, row = rownum)
#print('R:', rownum)
rownum += 1

lbl3 = Label(window, text="Choose Y-Column")
 
lbl3.grid(column=0, row = rownum )
#print('R:', rownum)
rownum += 1
 
# Only need one variable so that only one can be picked.
# yvar1 returns value variable setting, ie 1-4.
yvar1 = IntVar() 
rad1 = Radiobutton(window,text='Y1', value=1, variable = yvar1 )
rad2 = Radiobutton(window,text='Y2', value=2, variable = yvar1 )
rad3 = Radiobutton(window,text='Y3', value=3, variable = yvar1 )
rad4 = Radiobutton(window,text='Y4', value=4, variable = yvar1 )

rad1.grid(column=0, row = rownum )
rownum += 1
rad2.grid(column=0, row = rownum )
rownum += 1
rad3.grid(column=0, row = rownum )
rownum += 1
rad4.grid(column=0, row = rownum )
rownum += 1
#print('R:', rownum)

'''
'''

lblfilld = Label(window, text="")
 
lblfilld.grid(column=0, row = rownum)
#print('R:', rownum)
rownum += 1

btn = Button(window, text="Run", command=clicked )
 
btn.grid(column=0, row = rownum)
#print('R:', rownum)
rownum += 1

lblfillf = Label(window, text="")
 
lblfillf.grid(column=0, row = rownum)
#print('R:', rownum)
rownum += 1

lblfille = Label(window, text="")
 
lblfille.grid(column=0, row = rownum)
#print('R:', rownum)
rownum += 1

window.mainloop()
