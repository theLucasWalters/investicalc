import tkinter as tk
import tkinter.ttk as ttk
import functions as funcs

# percent change window

# init the pc window
def init_frame(window) -> ttk.Frame():
    pc_frame = ttk.Frame(window)

    # warn users to remove commas from their inputs
    warn = tk.Label(pc_frame, text="Make sure to remove all commas before pressing 'submit'")
    warn.pack()

    # create entry boxes for num1 & num2 and give placeholder values
    num1_label = tk.Label(pc_frame, text="Value 1:")
    num2_label = tk.Label(pc_frame, text="Value 2:")
    num1 = tk.Entry(pc_frame, width=20, borderwidth=2.5)
    num2 = tk.Entry(pc_frame, width=20, borderwidth=2.5)

    # pack entries
    num1_label.pack()
    num1.pack()
    num2_label.pack()
    num2.pack()

    # create and display a submit button
    calculate = tk.Button(pc_frame, text='Submit', command=lambda: funcs.percentChange(num1, num2, pc_frame).pack())
    calculate.pack()

    return pc_frame
