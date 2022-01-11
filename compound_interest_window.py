import tkinter as tk
import tkinter.ttk as ttk
import functions as funcs

# compound interest window

# init the ci window
def init_frame(window) -> ttk.Frame():
    ci_frame = ttk.Frame(window)

    # create labels and entries
    warn  = tk.Label(ci_frame, text='Enter all values as plain numbers. Letters and symbols will not be accepted.')
    warn2 = tk.Label(ci_frame, text='Decimals like 123.456 are okay, but 123/456 won\'t work.')
    initNum_label  = tk.Label(ci_frame, text='Initial Capital:')
    intRate_label  = tk.Label(ci_frame, text='Interest Rate:')
    compTime_label = tk.Label(ci_frame, text='Number of compounding periods:')
    initNum  = tk.Entry(ci_frame, width=40, borderwidth=2.5)
    intRate  = tk.Entry(ci_frame, width=40, borderwidth=2.5)
    compTime = tk.Entry(ci_frame, width=40, borderwidth=2.5)

    # *OptionMenu doesn't work*
    # create a menu for the user to pick how long the compounding periods are

    ## set the default for the dropdown to display
    unitVar = tk.StringVar()
    unitVar.set('Annually')

    ## create the array for the dropdown to contain
    units = [
        'Daily',
        'Weekly',
        'Monthly',
        'Quarterly',
        'Annually'
    ]

    ## create an arrow icon
    arrow = tk.PhotoImage(file='images/arrow.png') # <- arrow img credit: https://www.flaticon.com/authors/google

    ## create the actual dropdown
    unitMenu = tk.OptionMenu(ci_frame, unitVar, *units)
    ### set the icon
    unitMenu.image = arrow

    # create a calculate button
    calculate = tk.Button(ci_frame, text='Submit', command=lambda: funcs.compint(initNum, intRate, compTime, ci_frame).pack())

    # and pack everything in
    warn          .pack()
    warn2         .pack()
    initNum_label .pack()
    initNum       .pack()
    intRate_label .pack()
    intRate       .pack()
    unitMenu      .pack()
    compTime_label.pack()
    compTime      .pack()
    calculate     .pack()

    return ci_frame
