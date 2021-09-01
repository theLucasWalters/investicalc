from tkinter import *
import math

# create main window
root = Tk()
root.title('InvestiCalc')
root.iconbitmap('images/investicalc.ico') # <- icon downloaded from https://icon-icons.com/icon/stocks-graphic-with-a-magnifier-tool/70602
root.geometry('400x200')

def pick(var):
    if var.get() == 'Select a calculator:':
        return
    elif var.get() == 'Percent Change':
        percentChange_window()

# percent change calculator
def percentChange(num1, num2):
    # formula credit: https://www.calculatorsoup.com/calculators/algebra/percent-difference-calculator.php

    # change str inputs to float
    v1 = float(num1.get())
    v2 = float(num2.get())

    # calculate % change between v1 & v2 and round up to the 0.01%
    ans = ((v2 - v1) / abs(v1)) * 100
    rndANS = round(ans, 2)

    # display answer
    answer = Label(pc, text=f'Answer = {rndANS}%').pack()

# percent change calc window
def percentChange_window():
    # create PC (percent change) interface
    global pc
    pc = Tk()
    pc.title('Percent Change Calculator')
    pc.iconbitmap('images/investicalc.ico')
    pc.geometry('400x200')

    # warn users to remove commas from their inputs
    warn = Label(pc, text="Make sure to remove all commas before pressing 'submit'").pack()

    # create entry boxes for num1 & num2
    global num1, num2
    num1 = Entry(pc, width=20, borderwidth=2.5)
    num2 = Entry(pc, width=20, borderwidth=2.5)
    # display onscreen
    num1.pack(); num2.pack()

    # create and display a submit button
    calculate = Button(pc, text='Submit', command=lambda: percentChange(num1, num2))
    calculate.pack()

# create a dropdown menu to select a certain calculator

# set the default for the dropdown
var = StringVar()
var.set('Select a calculator:')

# set the different options
calcs = [
    'Percent Change',
]

# create and display menu
arrow = PhotoImage(file='images/arrow.png') # <- arrow img credit: https://www.flaticon.com/authors/google
options = OptionMenu(root, var, 'Select a calculator:', *calcs)
enter = Button(root, text='Go', command=lambda: pick(var))
options.pack()
enter.pack()

root.mainloop()
