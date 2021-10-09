from tkinter import *
import random

root=Tk() #root=tkinter.Tk()
root.geometry("500x400")
l=Label(root,font=("Helvetica",260))

def roll():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l.config(text=f'{random.choice(dice)}{random.choice(dice)}')
    l.pack()

b=Button(root,text="Roll the Dice!",foreground='blue',command=roll)
b.place(x=300,y=0)
b.pack()
 
root.mainloop()    



