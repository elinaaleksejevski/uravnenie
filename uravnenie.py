from tkinter import*
import tkinter as tk
from math import*
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def vorrand(a,b,c):
    D=b**2-4*a*c
    if D>0:
        x1=(-b+sqrt(D))/(2*a)
        x2=(-b-sqrt(D))/(2*a)
        text=(f'D = {D}\n Х1 = {round(x1,1)}\n и Х2 = {round(x2,1)}')
    elif D==0:
        x=(-b)/(2*a)
        text=(f'D ={D}\n = {x}' )
    else:
        text=('vastus puudub!')
    return text

def inserter(value):
    vastus.delete(0.0,END)
    vastus.insert(END,value)

def handler():
    try:
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        inserter(vorrand(a_val, b_val, c_val))
    except ValueError:
        inserter("Sisesta ainult arvud!")

def handler2():
    try:
        a_val = int(a.get())
        b_val = int(b.get())
        c_val = int(c.get())
        x1_val=int(x1.get())
        x2_val=int(x2.get())
        inserter(graafik(a_val, b_val, c_val,x1_val,x2_val))
    except TypeError:
        vstavka('Sisesta ainult arvud!')

def graafik(a,b,c,x1,x2):
    x = np.arange(x1,x2,0.5) 
    y1 = a*x**2 + b*x +c
    plt.subplots()
    plt.title(f"y = {a}x^2 + {b}*x + {c}")
    plt.xlabel("Ось абсцисс")
    plt.ylabel("Ось ординат")
    plt.xticks(np.arange(x1, x2, 1))
    plt.grid(True)
    plt.plot(x,y1 ,linewidth=3)
    plt.savefig("my_image.png")
    plt.show()
    return


root=Tk()
root.title('ruutvõrrandi lahendamine ja graafik')
root.geometry('400x200')
root.config(bg='grey')

a = Entry(root, width=3)
a.grid(row=0,column=0,padx=(10,0),stick='e')
a_lab = Label(root,bg='grey', text="x**2+",fg='white').grid(row=0,column=1,stick='e')
b = Entry(root, width=3)
b.grid(row=0,column=2)
b_lab = Label(root,bg='grey', text="x+",fg='white').grid(row=0, column=3,stick='w')
c = Entry(root, width=3)
c.grid(row=0, column=4)
c_lab = Label(root,bg='grey', text="= 0",fg='white').grid(row=0, column=5,stick='w')
 
btn_1 = Button(root, text="Arvuta!",command=handler).grid(row=0, column=6, padx=(10,0),pady=(10,10),rowspan=2)
btn_2 = Button(root, text="Joonista graafik!",command=handler2).grid(row=3, column=6, padx=(10,0),rowspan=2)

vastus = Text(root, bg="lightblue", font="Arial 12", width=30, height=3)
vastus.grid(row=2, columnspan=7,padx=10)
 
x1=Entry(root)
x2=Entry(root)
x1.grid(row=3,column=0,padx=10)
x2.grid(row=4,column=0,padx=10,pady=10)
lbl_x1=Label(root,text='Х1',bg='grey',fg='white').grid(row=3,column=1)
lbl_x2=Label(root,text='Х2',bg='grey',fg='white').grid(row=4,column=1)

root.mainloop()
