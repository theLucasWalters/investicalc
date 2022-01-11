import tkinter as tk
import tkinter.ttk as ttk
import functions as funcs
import datetime as dt # not being used yet
import percent_change_window as pc
import compound_interest_window as ci
import market_days_window as md

def main():
    # create main window
    root = tk.Tk()
    root.title('InvestiCalc')
    root.iconbitmap('images/investicalc.ico') # <- icon downloaded from https://icon-icons.com/icon/stocks-graphic-with-a-magnifier-tool/70602
    root.geometry('800x400')

    # set up notebook
    main = ttk.Notebook(root)
    main.pack(fill='both', expand=1)

    # declare frames to be assigned to tabs
    home     = ttk.Frame(main)
    pc_frame = pc.init_frame(main)
    ci_frame = ci.init_frame(main)
    md_frame = md.init_frame(main)

    # pack the frames in
    home    .pack(fill='both', expand=1)
    pc_frame.pack(fill='both', expand=1)
    ci_frame.pack(fill='both', expand=1)
    md_frame.pack(fill='both', expand=1)

    # declare tabs
    main.add(home, text='Home')
    main.add(pc_frame, text='Percent Change')
    main.add(ci_frame, text='Compound Interest')
    main.add(md_frame, text='Market Days')

    # hide the tabs from the start
    main.hide(1)
    main.hide(2)
    main.hide(3)

    # create buttons to open the tabs
    open_pc_btn = tk.Button(home, text='Calculate Percent Change', command=lambda: funcs.open_frame(main, 1))
    open_ci_btn = tk.Button(home, text='Calculate Compound Interest', command=lambda: funcs.open_frame(main, 2))
    open_md_btn = tk.Button(home, text='View Market Days', command=lambda: funcs.open_frame(main, 3))

    # pack the buttons
    open_pc_btn.pack()
    open_ci_btn.pack()
    open_md_btn.pack()

    # loop
    root.mainloop()

if __name__ == '__main__':
    main()
