#Relogio Digital com Python

from tkinter import *
from time import strftime

def tic():
    rel['text'] = strftime('%H:%M:%S')


def tac():
    tic()
    rel.after(1000, tac)

j = Tk()

rel = Label(j, font='helvetica 100')
rel.pack()
tac()

j.mainloop()