# ░▓

from tkinter import *

master = Tk()
master.title('Revmeter')
master.geometry('400x200')
master.resizable(False, False)

# BKG
#bkg = PhotoImage(file='enter bkg image file name here')
#setb = Label(master, image=bkg)
#setb.place(x=0, y=0, relwidth=1, relheight=1)
rpmvar = StringVar(master)
l1 = Label(master, text=rpmvar).grid(row=0, column=0)
rpm = 0

while True:
    if rpm > 6000:
        rpm = 0
    else:
        rpm += 1
    rpmvar.set(rpm)

 







def clr(event):
  event.widget.delete(0, 'end')
  return None

#e1 = Entry(master, highlightthickness=0, width=30)
#e1.insert(0,'Enter default text here')
#e1.bind('<FocusIn>', clr)

#e1.grid(row=1, column=0, pady=0)

# ENTRY

# BUTTON

#b1 = Button(master, text='Enter button text here', command=enter name of function here, width=1).grid(row=2, column=0, sticky=W, pady=4)

# BUTTON





master.mainloop()
