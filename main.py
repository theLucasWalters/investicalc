from tkinter import *
from tkinter import ttk

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
    ansLabel = Label(pc_frame, text=f'Answer = {rndANS}%').pack()

# compound interest calculation
def compint(initNum, intRate, compTime):
    # formula credit: https://www.investopedia.com/terms/c/compoundinterest.asp

    # turn initNum.get() from str -> float
    principal = float(initNum.get())

    # do the same with intRate.get() & divide by 100
    rate = float(intRate.get()) / 100

    # use float or int accordingly for compTime.get()
    try:
        time = int(compTime.get())
    except:
        time = float(compTime.get())

    # calculate, round, and display
    answer = (principal * ((1 + rate) ** time) - 1)
    rndANS = round(answer, 2)
    ansLabel = Label(ci_frame, text=f'After {time} compounding periods, you will have ${rndANS}').pack()

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
def on_click_v1(event):
    num1.config(state=NORMAL)
    num1.delete(0, END)
    num1.unbind('<Button-1>', on_click_num1)
def on_click_v2(event):
    num2.config(state=NORMAL)
    num2.delete(0, END)
    num2.unbind('<Button-1>', on_click_num2)

# open percent change and compound interest accordingly
def open_pc():
    main.select(1)
def open_ci():
    main.select(2)

# create main window
root = Tk()
root.title('InvestiCalc')
root.iconbitmap('images/investicalc.ico') # <- icon downloaded from https://icon-icons.com/icon/stocks-graphic-with-a-magnifier-tool/70602
root.geometry('800x400')

# set up notebook
main = ttk.Notebook(root)
main.pack(fill='both', expand=1)

# declare frames to be assigned to tabs
home = Frame(main)
pc_frame = Frame(main)
ci_frame = Frame(main)

# pack the frames in
home.pack(fill='both', expand=1)
pc_frame.pack(fill='both', expand=1)
ci_frame.pack(fill='both', expand=1)

# declare tabs
main.add(home, text='Home')
main.add(pc_frame, text='Percent Change')
main.add(ci_frame, text='Compound Interest')

# hide the tabs from the start
main.hide(1); main.hide(2)

# create buttons to open the tabs
open_pc_btn = Button(home, text='Calculate Percent Change', command=open_pc)
open_ci_btn = Button(home, text='Calculate Compound Interest', command=open_ci)

# pack the buttons
open_pc_btn.pack()
open_ci_btn.pack()

########################
# Percent Change window
########################

# warn users to remove commas from their inputs
warn = Label(pc_frame, text="Make sure to remove all commas before pressing 'submit'").pack()

# create entry boxes for num1 & num2 and give placeholder values
num1 = Entry(pc_frame, width=20, borderwidth=2.5)
num2 = Entry(pc_frame, width=20, borderwidth=2.5)
num1.insert(0, 'Starting value')
num2.insert(0, 'Ending value')
num1.config(state=DISABLED)
num2.config(state=DISABLED)
on_click_num1 = num1.bind('<Button-1>', on_click_v1)
on_click_num2 = num2.bind('<Button-1>', on_click_v2)

# pack entries
num1.pack(); num2.pack()

# create and display a submit button
calculate = Button(pc_frame, text='Submit', command=lambda: percentChange(num1, num2))
calculate.pack()

###########################
# Compound Interest window
###########################

# declare initial investment
initNum = Entry(ci_frame, width=40, borderwidth=2.5)
initNum.insert(0, 'Initial capital')
initNum.config(state=DISABLED)
on_click_initnum = initNum.bind('<Button-1>', on_click_IN)

# declare interest rate
intRate = Entry(ci_frame, width=40, borderwidth=2.5)
intRate.insert(0, 'Interest rate')
intRate.config(state=DISABLED)
on_click_intRate = intRate.bind('<Button-1>', on_click_IR)

# declare the number of compounding periods
compTime = Entry(ci_frame, width=40, borderwidth=2.5)
compTime.insert(0, "Number of compounding periods")
compTime.config(state=DISABLED)
on_click_compTime = compTime.bind('<Button-1>', on_click_T)

# clarify if compounding will be daily, weekly, monthly, quarterly, or annually
unitVar = StringVar()
unitVar.set('Annually')
units = [
    'Daily',
    'Weekly',
    'Monthly',
    'Quarterly',
    'Annually',
]

# create OptionMenu for user clarity; doesn't actually affect calculation
unitMenu = OptionMenu(ci_frame, unitVar, *units)

# will figure out how to use the arrow for the OptionMenu icon later
arrow = PhotoImage(file='images/arrow.png') # <- arrow img credit: https://www.flaticon.com/authors/google

# submit button to calculate CI
calculate = Button(ci_frame, text='Submit', command=lambda: compint(initNum, intRate, compTime))

# pack everything in
initNum.pack()
intRate.pack()
unitMenu.pack()
compTime.pack()
calculate.pack()

# loop
root.mainloop()
