from tkinter import *
import math

root = Tk()
root.title('InvestiCalc')
root.iconbitmap('images/investicalc.ico') # <- icon downloaded from https://icon-icons.com/icon/stocks-graphic-with-a-magnifier-tool/70602
root.geometry('400x200')

def percentChange(num1, num2):
    # percent change calculator
    # formula credit: https://www.calculatorsoup.com/calculators/algebra/percent-difference-calculator.php

    global v1, v2
    v1 = float(num1.get())
    v2 = float(num2.get())

    ans = ((v2 - v1) / abs(v1)) * 100
    rndANS = round(ans, 2)

    answer = Label(pc, text=f'Answer = {rndANS}%').pack()

def percentChange_window():
    # percent change calc window

    global pc
    pc = Tk()
    pc.title('Percent Change Calculator')
    pc.iconbitmap('images/investicalc.ico')
    pc.geometry('400x200')

    warn = Label(pc, text="Make sure to remove all commas before pressing 'submit'").pack()
    num1 = Entry(pc, width=20, borderwidth=2.5)
    num2 = Entry(pc, width=20, borderwidth=2.5)
    num1.pack(); num2.pack()
    calculate = Button(pc, text='Submit', command=lambda: percentChange(num1, num2))
    calculate.pack()

var = StringVar()
var.set('Select a calculator:')

calcs = [
    'Percent Change',
]

arrow = PhotoImage(file='images/arrow.png') # <- arrow img credit: https://www.flaticon.com/authors/google
options = OptionMenu(root, var, 'Select a calculator:', *calcs)
enter = Button(root, text='Go', command=percentChange_window)

options.pack()
enter.pack()

root.mainloop()
