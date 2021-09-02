from tkinter import *

# create main window
root = Tk()
root.title('InvestiCalc')
root.iconbitmap('images/investicalc.ico') # <- icon downloaded from https://icon-icons.com/icon/stocks-graphic-with-a-magnifier-tool/70602
root.geometry('400x200')

# pick the selected calculator from options
def pick(var):
    if var.get() == 'Select a calculator:':
        return
    elif var.get() == 'Percent Change':
        percentChange_window()
    elif var.get() == 'Compound Interest':
        compInt_window()

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
    ansLabel = Label(pc, text=f'Answer = {rndANS}%').pack()

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

# comp interest calc window
def compInt_window():
    global ci
    ci = Tk()
    ci.title('Compound Interest Calculator')
    ci.iconbitmap('images/investicalc.ico')
    ci.geometry('400x200')

    # declare initial investment
    global initNum, intRate, compTime
    global on_click_initnum, on_click_intRate, on_click_compTime
    initNum = Entry(ci, width=40, borderwidth=2.5)
    initNum.insert(0, 'Initial capital')
    initNum.config(state=DISABLED)
    on_click_initnum = initNum.bind('<Button-1>', on_click_IN)

    # declare interest rate
    intRate = Entry(ci, width=40, borderwidth=2.5)
    intRate.insert(0, 'Interest rate')
    intRate.config(state=DISABLED)
    on_click_intRate = intRate.bind('<Button-1>', on_click_IR)

    # declare the number of compounding periods
    compTime = Entry(ci, width=40, borderwidth=2.5)
    compTime.insert(0, "Number of compounding periods")
    compTime.config(state=DISABLED)
    on_click_compTime = compTime.bind('<Button-1>', on_click_T)

    # clarify if compounding will be daily, weekly, monthly, quarterly, or annually
    ## can't get "unitVar.set('Annually')" to display correctly and 
    ## I'm too tired to figure it out this time around
    unitVar = StringVar()
    unitVar.set('Annually')
    units = [
        'Daily',
        'Weekly',
        'Monthly',
        'Quarterly',
        'Annually',
    ]
    unitMenu = OptionMenu(ci, unitVar, *units)

    # submit button to calculate CI
    calculate = Button(ci, text='Submit', command=lambda: compint(initNum, intRate, compTime))

    # pack everything in
    initNum.pack()
    intRate.pack()
    unitMenu.pack()
    compTime.pack()
    calculate.pack()

# compound interest calculation
def compint(initNum, intRate, compTime):
    principal = float(initNum.get())
    rate = float(intRate.get()) / 100
    try:
        time = int(compTime.get())
    except:
        time = float(compTime.get())

    answer = (principal * ((1 + rate) ** time) - 1)
    rndANS = round(answer, 2)

    ansLabel = Label(ci, text=f'After {time} compounding periods, you will have ${rndANS}').pack()

# remove placeholder text when clicking the Entry
def on_click_IN(event):
    initNum.config(state=NORMAL)
    initNum.delete(0, END)
    initNum.unbind('<Button-1>', on_click_initnum)

def on_click_IR(event):
    intRate.config(state=NORMAL)
    intRate.delete(0, END)
    intRate.unbind('<Button-1>', on_click_intRate)

def on_click_T(event):
    compTime.config(state=NORMAL)
    compTime.delete(0, END)
    compTime.unbind('<Button-1>', on_click_compTime)

# create a dropdown menu to select a certain calculator

# set the default for the dropdown
var = StringVar()
var.set('Select a calculator:')

# set the different options
calcs = [
    'Percent Change',
    'Compound Interest',
]

# create and display menu
global arrow
arrow = PhotoImage(file='images/arrow.png') # <- arrow img credit: https://www.flaticon.com/authors/google
options = OptionMenu(root, var, 'Select a calculator:', *calcs)
enter = Button(root, text='Go', command=lambda: pick(var))
options.pack()
enter.pack()

root.mainloop()
