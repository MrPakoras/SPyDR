# Add save file
# Save money and unlocked parts
# Eg. Read unlocked and locked engines file to lists
# If engine purchased, move to unlocked list
# At save, write locked and unlocked to save file to be read from next time

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
#subtitle = Label(titleframe, text='Super Python Drag Racer', bg='#420051', fg='white')
#subtitle.pack(fill=x, expand=1)

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

# 'Username' text label
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

# 'Money' text label
moneytext = Label(if3, text='MONEY:',anchor='e')
moneytext.pack(fill=X, expand=1)

# Money label
money = 0
moneyvar = StringVar(if4)
moneytext = '£'+str(money)
moneyvar.set(moneytext)
moneylab = Label(if4, textvariable=moneyvar)
moneylab.pack(fill=X, expand=1)

# Widgets and Output Box Master Frame
waomframe = Frame(master, height=250, width=800,bg='black')
waomframe.pack_propagate(0)
waomframe.grid(row=2,column=0,sticky='w')

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

### Message Box
messframe = Frame(waomframe, width=200, height=49)
messframe.pack_propagate(0)
messframe.grid(row=1,column=0,sticky='new')

messlab = Label(messframe, text='Warning: Using Nitrous may cause engine failiures.', fg='red', bg='black')
messlab.pack(fill=BOTH, expand=1)

# Build Car Button
def build():
    chasph = chasddvar.get()
    engph = engddvar.get()
    nitph = nitddvar.get()
    
    if chasph == chasddselect or engph == engddselect or nitph == nitddselect:
        outvarph = 'Error. Please select parts for your car...'
        outvar.set(outvarph)
    else:
        outvarph = ('''Your car has been built!\n\n
Chassis: '''+chasph+'\nEngine: '+engph+'\nNitrous: '+nitph)
        outvar.set(outvarph)
        outtext.pack(fill=BOTH, expand=1)

        rbutton.config(state='normal')
    
build = Button(widframe, command=build, text='BUILD', bg='#3c3c3c', fg='yellow',activebackground='#2b2b2b',activeforeground='yellow')
build.grid(row=3, column=1, sticky='news')

### Race Button GUI
rbuttonvar = StringVar(rbframe)
rbuttonvar.set('START RACE')
rbutton = Button(rbframe, text=rbuttonvar.get(), command=start, bg='#3c3c3c', fg='lime',activebackground='#2b2b2b',activeforeground='lime')
rbutton.config(state='disabled')
rbutton.pack(fill=BOTH, expand=1)

# Shift Button Frame
shframe = Frame(btnframe, height=50, width=200,bg='black')
shframe.pack_propagate(0)
shframe.grid(row=0,column=1)

# Shift Button GUI    
shvar = IntVar()
shbutton = Button(shframe, text='SHIFT', command=lambda: shvar.set(1), bg='#3c3c3c', fg='red',activebackground='#2b2b2b',activeforeground='red')
shbutton.config(state='disabled')
shbutton.pack(fill=BOTH, expand=1)
    

### CODE ###


# Finding Opponent            
def findingopp():
    outvarph = 'Finding opponent, please wait...'
    outvar.set(outvarph)
    print('finding')

#  Found Opponent
def foundopp():
    outvarph = 'Opponent found. Race commencing in 5 seconds...\n\n'
    
    co = random.choice(cl)
    eo = random.choice(el)
    nit = random.choice(['y','n'])
    global avgo
    avgo = round(random.uniform(0,0.8),3)

    nitph = nitddvar.get()
    if nitph != 'None':
        fail = random.randint(1,3)
        if fail == 1:
            avgo += random.uniform(0.2,0.5)
            avgo = round(avgo,3)

    oppdata = ('Your opponent has a:\n'+co+'\n'+'with a '+eo)
    outvar.set(outvarph+oppdata)
    print('found')
# Start Race Button
def start():
    build.config(state='disabled')
    prog()
    #shbutton.config(state='normal')
# Start Now Text
def startnow():
    shbutton.config(state='normal')
    outvarph = 'Drag race starts NOW!'
    outvar.set(outvarph)


###   Needs working on:
# Shifloop
def shiftloop():
    t1 = time.perf_counter()
    outvar.set('SHIFT NOW!')

    shbutton.wait_variable(shvar)

    t = round(time.perf_counter()-t1,3)
    times += t
    outvarph = ('Gear Shift took '+str(t)+' seconds\n')
    outvar.set(outvarph)
# Shiftcode
def shiftcode():
    global times
    global avg
    shiftdata = ''
    times = 0

    for loop in range(5):
        shwait = random.randint(1,5)*1000
        master.after(shwait,shiftloop)

    avg = round(times/5,3)
    outvarph = ('\n\nYour Average shift time was: '+str(avg))
    outvar.set(outvarph)
    outvarph = 'Your shifting speed was '
    if 0<avg<0.2:
        outvarph+'awesome'
    elif 0.3<avg<0.4:
        outvarph+'good'
    elif 0.4<avg<0.7:
        outvarph+'poor'
    elif avg>0.7:
        outvarph+'not worth waiting for'
    outvar.set(outvarph)

    nitph = nitddvar.get()
    if nitph != 'None':
        fail = random.randint(1,3)
        if fail == 1:
            times += random.uniform(0.2,0.5)
            avg = round(times/5,3)
            outvarph = ('Oh dear. You have blown a head gasket. Therefore your actual time was: '+str(avg))
            outvar.set(outvarph)

# Shift
def shift():
    global t, t1, times, outvar
    t = round(time.perf_counter()-t1,3)
    times += t
    outvarph = ('Gear Shift took '+str(t)+' seconds\n')
    outvar.set(outvarph)

# Results (end of game and money dealt)
def results():
    global money, avg
    if avg < avgo:
        prize = random.randint(100,1000)
        money += prize
        moneytext = '£'+str(money)
        moneyvar.set(moneytext)
        outvarph = ('You won by '+str(round(avgo-avg, 3))+' seconds.\nCongratulations on the win. Here is £'+str(prize)+' as a reward.')
        outvar.set(outvarph)
    else:
        outvarph = ('You lost by '+str(round(avg-avgo, 3))+' seconds unfortunately.\nBetter luck next time.')
        outvar.set(outvarph)

### Program
def prog():
    rbutton.config(state='disabled')
    global oppdata, outvar, avg, avgo
    
    num = 1
    
    outvarph = '''Get ready to drag race...
    Wait for the "SHIFT NOW!" signal and click the "SHIFT" button to shift up a gear.'''
    outvar.set(outvarph)
    print('ready')

    master.after(2000, findingopp)
    master.after(5000, foundopp)
    master.after(10000, startnow)

    #################
    #shiftcode()
    #################
    
    # opptime = ('Your opponent clocked in at '+str(avgo)+' seconds.')

    shbutton.config(state='disabled')
    rbutton.config(state='normal')
    build.config(state='normal')



### BUTTONS ###




#  Play Again code
#    p = input('Race again? y or n:   ')
#    if p == 'y':
#        print('\n\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\n')
#        prog()
#    else:
#        quit()

# master.protocol('WM_DELETE_WINDOW',nothing()) #On exit event


master.mainloop()


