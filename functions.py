from tkinter import *

# percent change calculator
def percentChange(num1, num2, frame):
    # formula credit: https://www.calculatorsoup.com/calculators/algebra/percent-difference-calculator.php

    # change str inputs to float
    v1 = float(num1.get())
    v2 = float(num2.get())

    # calculate % change between v1 & v2 and round up to the 0.01%
    ans = ((v2 - v1) / abs(v1)) * 100
    rndANS = round(ans, 2)

    # display answer
    ansLabel = Label(frame, text=f'Answer = {rndANS}%').pack()

# compounding calculator
def compint(initNum, intRate, compTime, frame):
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
    ansLabel = Label(frame, text=f'After {time} compounding periods, you will have ${rndANS}').pack()

# open frames as needed
def open_frame(frame, frame_num):
    frame.select(frame_num)
