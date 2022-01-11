import tkinter as tk
import tkinter.ttk as ttk

# market days window

def init_frame(window) -> ttk.Frame():
    md_frame = ttk.Frame(window)

    hi_label = tk.Label(md_frame, text='Hi! There\'s nothing here yet.')
    hi_label.pack()

    return md_frame
