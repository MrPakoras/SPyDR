import time, random
from tkinter import *

# Master
master = Tk()
master.title('SPyDR v1.0')
master.geometry('800x450')
# master.wm_attributes('-transparentcolor', master['bg'])
master.resizable(False, False)

# Background
bkg = PhotoImage(file='bkg2.gif')
setb = Label(master, image=bkg)
setb.place(x=0, y=0, relwidth=1, relheight=1)

# Title Widgets
titleframe = Frame(master, height=30, width=800, bg='black')
titleframe.pack_propagate(0)
titleframe.grid(row=0,column=0)

title = Label(titleframe, text='SPyDR', bg='#420051', fg='white')
title.pack(fill=X, expand=1)

# Shift Button Frame
shframe = Frame(master, height=50, width=200,bg='black')
shframe.pack_propagate(0)
shframe.grid(row=2,column=0)

###

waitvar = IntVar()
global shiftime
shifttime = 0

def revmeter():
	global shifttime
	shifttime = 0
	for loop in range(5):
		time.sleep(random.uniform(0.5,3))
		print('Shift Now!')
		x = time.time()
		#print(x)
		#shbutton.wait_variable(waitvar)
		y = time.time()
		#print(y)
		z = y-x
		print(z)
		shifttime += z



shbutton = Button(shframe, text='SHIFT', command=lambda: waitvar.set(1), bg='#3c3c3c', fg='red',activebackground='#2b2b2b',activeforeground='red')
shbutton.pack(fill=BOTH, expand=1)


revmeter()

print('\n\nShifttime:   '+str(shifttime))
print('Avg Shifttime:   '+str(shifttime/5))

master.mainloop()