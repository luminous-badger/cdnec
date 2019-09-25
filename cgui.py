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
#from ncd import proc_cons4b 
#import ncd 
import cdsdirb
# Need new name for above procs.
# just import filename and use that to prefix func name.

csvlist = [ ]

flist = os.listdir( './' )
for f in ( flist ):
    if ( f.endswith( '.csv' ) ):
        csvlist.append( f )
	# Only append csv files for combo box file choice.

rownum = 0
 
def clicked():
	fname = combofn.get()  
	Yval = yvar1.get() 
	msg = 'Running ' + fname + ' Y: ' + str( Yval ) + ' Suff'
	lblfille.configure(text = msg )
	#ncd.proc_cons4b( fname, Yval )
	cdsdirb.suff_main( fname, Yval )
	#print( 'FName:', combofn.get(), ' Ty:', type( combofn.get() ) )
	#print( 'XCols:', comboxc.get() )
	#print( 'Yval1:', yvar1.get() )

window = Tk()
 
window.title("FSGOF")
window.geometry('350x550')
 
lbl = Label(window, text="Fuzzy Set Goodness of Fit")
 
lbl.grid(column=0, row=rownum)
#print('R:', rownum)
rownum += 1
 
lblfillbfrqca = Label(window, text="")
 
lblfillbfrqca.grid(column=0, row=rownum)
#print('R:', rownum)
rownum += 1
 
lblqca = Label(window, text="Qualitative Comparitive Analysis")
 
lblqca.grid(column=0, row=rownum)
#print('R:', rownum)
rownum += 1
 
lblfilla = Label(window, text="")
 
lblfilla.grid(column=0, row=rownum)
#print('R:', rownum)
rownum += 1
 
lbl2 = Label(window, text="Choose a File Name")
 
lbl2.grid(column=0, row = rownum )
#print('R:', rownum)
rownum += 1

lblfillc = Label(window, text="")
 
lblfillc.grid(column=0, row=rownum)
#print('R:', rownum)
rownum += 1
 
combofn = Combobox(window)
combofn['values'] = csvlist 
combofn.current(0) #set the selected item
combofn.grid(column=0, row = rownum )
#print('R:', rownum)
rownum += 1

lblfillb = Label(window, text="")
 
lblfillb.grid(column=0, row = rownum)
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

lblfillfda = Label(window, text="")
 
lblfillfda.grid(column=0, row = rownum)
#print('R:', rownum)
rownum += 1

lblfilld = Label(window, text="  Choose: Sufficient, Necessary or Both")
 
lblfilld.grid(column=0, row = rownum)
#print('R:', rownum)
rownum += 1

snvar1 = IntVar() 
rad5 = Radiobutton(window,text='Sufficient', value=1, variable = snvar1 )
rad6 = Radiobutton(window,text=' Necessary', value=2, variable = snvar1 )
rad7 = Radiobutton(window,text='Both      ', value=3, variable = snvar1 )

rad5.grid(column=0, row = rownum )
rownum += 1
rad6.grid(column=0, row = rownum )
rownum += 1
rad7.grid(column=0, row = rownum )
rownum += 1

lblfillfa = Label(window, text="")
 
lblfillfa.grid(column=0, row = rownum)
#print('R:', rownum)
rownum += 1

lblfillc = Label(window, text="")
 
lblfillc.grid(column=0, row = rownum)
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
