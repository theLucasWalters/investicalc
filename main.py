import tkinter as tk
import tkinter.ttk as ttk
import functions as funcs
# import datetime as dt # not being used yet
# import percent_change_window as pc # not being used yet
# import compound_interest_window as ci # not being used yet

# remove placeholder text when clicking the Entry
def on_click_IN(event):
    initNum.config(state=tk.NORMAL)
    initNum.delete(0, tk.END)
    initNum.unbind('<Button-1>', on_click_initnum)
def on_click_IR(event):
    intRate.config(state=tk.NORMAL)
    intRate.delete(0, tk.END)
    intRate.unbind('<Button-1>', on_click_intRate)
def on_click_T(event):
    compTime.config(state=tk.NORMAL)
    compTime.delete(0, tk.END)
    compTime.unbind('<Button-1>', on_click_compTime)
def on_click_v1(event):
    num1.config(state=tk.NORMAL)
    num1.delete(0, tk.END)
    num1.unbind('<Button-1>', on_click_num1)
def on_click_v2(event):
    num2.config(state=tk.NORMAL)
    num2.delete(0, tk.END)
    num2.unbind('<Button-1>', on_click_num2)

# create main window
root = tk.Tk()
root.title('InvestiCalc')
root.iconbitmap('images/investicalc.ico') # <- icon downloaded from https://icon-icons.com/icon/stocks-graphic-with-a-magnifier-tool/70602
root.geometry('800x400')

# set up notebook
main = ttk.Notebook(root)
main.pack(fill='both', expand=1)

# declare frames to be assigned to tabs
home = ttk.Frame(main)
pc_frame = ttk.Frame(main)
ci_frame = ttk.Frame(main)
market_days = ttk.Frame(main)

# pack the frames in
home.pack(fill='both', expand=1)
pc_frame.pack(fill='both', expand=1)
ci_frame.pack(fill='both', expand=1)

# declare tabs
main.add(home, text='Home')
main.add(pc_frame, text='Percent Change')
main.add(ci_frame, text='Compound Interest')

# hide the tabs from the start
main.hide(1)
main.hide(2)

# create buttons to open the tabs
open_pc_btn = tk.Button(home, text='Calculate Percent Change', command=lambda: funcs.open_frame(main, 1))
open_ci_btn = tk.Button(home, text='Calculate Compound Interest', command=lambda: funcs.open_frame(main, 2))

# pack the buttons
open_pc_btn.pack()
open_ci_btn.pack()

########################
# Percent Change window
########################

# warn users to remove commas from their inputs
warn = tk.Label(pc_frame, text="Make sure to remove all commas before pressing 'submit'").pack()

# create entry boxes for num1 & num2 and give placeholder values
num1 = tk.Entry(pc_frame, width=20, borderwidth=2.5)
num2 = tk.Entry(pc_frame, width=20, borderwidth=2.5)
num1.insert(0, 'Starting value')
num2.insert(0, 'Ending value')
num1.config(state=tk.DISABLED)
num2.config(state=tk.DISABLED)
on_click_num1 = num1.bind('<Button-1>', on_click_v1)
on_click_num2 = num2.bind('<Button-1>', on_click_v2)

# pack entries
num1.pack()
num2.pack()

# create and display a submit button
calculate = tk.Button(pc_frame, text='Submit', command=lambda: funcs.percentChange(num1, num2, pc_frame))
calculate.pack()

###########################
# Compound Interest window
###########################

# declare initial investment
initNum = tk.Entry(ci_frame, width=40, borderwidth=2.5)
initNum.insert(0, 'Initial capital')
initNum.config(state=tk.DISABLED)
on_click_initnum = initNum.bind('<Button-1>', on_click_IN)

# declare interest rate
intRate = tk.Entry(ci_frame, width=40, borderwidth=2.5)
intRate.insert(0, 'Interest rate')
intRate.config(state=tk.DISABLED)
on_click_intRate = intRate.bind('<Button-1>', on_click_IR)

# declare the number of compounding periods
compTime = tk.Entry(ci_frame, width=40, borderwidth=2.5)
compTime.insert(0, "Number of compounding periods")
compTime.config(state=tk.DISABLED)
on_click_compTime = compTime.bind('<Button-1>', on_click_T)

# clarify if compounding will be daily, weekly, monthly, quarterly, or annually
unitVar = tk.StringVar()
unitVar.set('Annually')
units = [
    'Daily',
    'Weekly',
    'Monthly',
    'Quarterly',
    'Annually',
]

# create OptionMenu for user clarity; doesn't actually affect calculation at the moment (will use later)
unitMenu = tk.OptionMenu(ci_frame, unitVar, *units)

# will figure out how to use the arrow for the OptionMenu icon later
arrow = tk.PhotoImage(file='images/arrow.png') # <- arrow img credit: https://www.flaticon.com/authors/google

# submit button to calculate CI
calculate = tk.Button(ci_frame, text='Submit', command=lambda: funcs.compint(initNum, intRate, compTime, ci_frame))

# pack everything in
initNum.pack()
intRate.pack()
unitMenu.pack()
compTime.pack()
calculate.pack()

###########################
# Market days window
###########################

# nothing here yet

# loop
root.mainloop()
