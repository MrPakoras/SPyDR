import time, random
from tkinter import *

# Chassis File
c = open('Chassis.txt','r').read()
cl = c.split('\n')

# Engine File
e = open('Engines.txt','r').read()
el = e.split('\n')

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


### Info (Username and Money)
# Master Info Frame
ifm = Frame(master, height=45, width=800)
ifm.pack_propagate(0)
ifm.grid(row=1,column=0,sticky='w')

# Info Frame 1
if1 = Frame(ifm, height=45, width=200)
if1.pack_propagate(0)
if1.grid(row=0,column=0,sticky='w')

# Info Frame 2
if2 = Frame(ifm, height=45, width=200)
if2.pack_propagate(0)
if2.grid(row=0,column=1,sticky='w')

# Info Frame 3
if3 = Frame(ifm, height=45, width=200)
if3.pack_propagate(0)
if3.grid(row=0,column=2,sticky='w')

# Info Frame 4
if4 = Frame(ifm, height=45, width=200)
if4.pack_propagate(0)
if4.grid(row=0,column=3,sticky='w')

### 'Username' text label
userlab = Label(if1, text='USER:')
userlab.pack(fill=X, expand=1)

# Username entry field
def clr(event):
    event.widget.delete(0, 'end')
    return None

userent = Entry(if2)
userent.insert(0,'Enter Username')
userent.bind('<FocusIn>', clr)
userent.pack(fill=BOTH, expand=1)
#user = userent.get()

### 'Money' text label
moneytext = Label(if3, text='MONEY:',anchor='e')
moneytext.pack(fill=X, expand=1)

# Money label
money = 0
moneyvar = StringVar(if4)
moneytext = '£'+str(money)
moneyvar.set(moneytext)
moneylab = Label(if4, textvariable=moneyvar)
moneylab.pack(fill=X, expand=1)

### Widgets and Output Box Master Frame
waomframe = Frame(master, height=250, width=800,bg='black')
waomframe.pack_propagate(0)
waomframe.grid(row=2,column=0,sticky='w')

#############################################################################################
## ~~ CODE HERE ~~ ##

def build():
	pass

def start():
	pass



##############################################################################################

### Car Modification Widgets
widframe = Frame(waomframe, height=250, width=400, bg='black')
widframe.pack_propagate(0)
widframe.grid(row=0,column=0,sticky='news')

# Chassis Widgets
chaslab = Label(widframe, text='CHASSIS:', width=27, bg='black', fg='white', relief=SUNKEN).grid(row=0, column=0, sticky='news')
chasddvar = StringVar(widframe)
chasddselect = '--Select Chassis--'
chasddvar.set(chasddselect) # Starting text
chasdd = OptionMenu(widframe, chasddvar, *cl) # *cl = list of options from chassis.txt
chasdd.config(width=27)
chasdd.grid(row=0,column=1)

# Engine Widgets
englab = Label(widframe, text='ENGINE:', bg='black', fg='white', relief=SUNKEN).grid(row=1, column=0, sticky='news')
engddvar = StringVar(widframe)
engddselect = '--Select Engine--'
engddvar.set(engddselect)
engdd = OptionMenu(widframe, engddvar, *el).grid(row=1,column=1, sticky='ew')

# Nitrous Widgets
nitlab = Label(widframe, text='NITROUS:', bg='black', fg='white', relief=SUNKEN).grid(row=2, column=0, sticky='news')
nitddvar = StringVar(widframe)
nitddselect = '--Select Nitrous--'
nitddvar.set(nitddselect)
nl = ['None','5l Tank']
nitdd = OptionMenu(widframe, nitddvar, *nl).grid(row=2,column=1, sticky='ew')

build = Button(widframe, command=build, text='BUILD', bg='#3c3c3c', fg='yellow',activebackground='#2b2b2b',activeforeground='yellow')
build.grid(row=3, column=1, sticky='news')


### Output Box
opframe = Frame(waomframe, height=200, width=400, relief=SUNKEN, bg='black')
opframe.pack_propagate(0)
opframe.grid(row=0,column=1,sticky='e')

outvar = StringVar(master)
outvarph = '''Welcome to the SPyDR drag strip.
Please build your car to be raced.'''
outvar.set(outvarph)
outtext = Label(opframe, textvariable=outvar, fg='cyan', bg='black', justify=CENTER, relief=SUNKEN)
outtext.pack(fill=BOTH, expand=1)

### Race and Shift Buttons
# RaS Master Frame
btnframe = Frame(waomframe, height=50, width=400, bg='black')
btnframe.pack_propagate(0)
btnframe.grid(row=1,column=1)

# Start Race Button Frame
rbframe = Frame(btnframe, height=50, width=200,bg='black')
rbframe.pack_propagate(0)
rbframe.grid(row=0,column=0)

rbuttonvar = StringVar(rbframe)
rbuttonvar.set('START RACE')
rbutton = Button(rbframe, text=rbuttonvar.get(), command=start, bg='#3c3c3c', fg='lime',activebackground='#2b2b2b',activeforeground='lime')
rbutton.config(state='disabled')
rbutton.pack(fill=BOTH, expand=1)

# Shift Button Frame
shframe = Frame(btnframe, height=50, width=200,bg='black')
shframe.pack_propagate(0)
shframe.grid(row=0,column=1)
shvar = IntVar()
shbutton = Button(shframe, text='SHIFT', command=lambda: shvar.set(1), bg='#3c3c3c', fg='red',activebackground='#2b2b2b',activeforeground='red')
shbutton.config(state='disabled')
shbutton.pack(fill=BOTH, expand=1)

### Message Box
messframe = Frame(waomframe, width=200, height=49)
messframe.pack_propagate(0)
messframe.grid(row=1,column=0,sticky='new')

messlab = Label(messframe, text='Warning: Using Nitrous may cause engine failiures.', fg='red', bg='black')
messlab.pack(fill=BOTH, expand=1)

master.mainloop()