import tkinter as tk

firstNum = 0
secondNum = 0
clicksInfo = list()
firstNumDigits = 0
secondNumDigits = 0
seenNumbers = ""


def buttonClicked(numOrSym, isANumber):
    global clicksInfo
    clicksInfo.append(numOrSym)
    print(clicksInfo)

def resetLabel():
    global clicksInfo, firstNumDigits, secondNumDigits, seenNumbers
    clicksInfo.clear()
    firstNumDigits = 0
    secondNumDigits = 0
    seenNumbers = ""
    label.config(text=seenNumbers)

window = tk.Tk()
window.title("Calculadora")
label = tk.Label(window, text="0", padx=60, pady=20)
button_clear = tk.Button(window, text="C", padx=20, pady=20, command=resetLabel)
button_0 = tk.Button(window, text="0", padx=20, pady=20, command=lambda:buttonClicked(0,True))
button_1 = tk.Button(window, text="1", padx=20, pady=20, command=lambda:buttonClicked(1,True))
button_2 = tk.Button(window, text="2", padx=20, pady=20, command=lambda:buttonClicked(2,True))
button_3 = tk.Button(window, text="3", padx=20, pady=20, command=lambda:buttonClicked(3,True))
button_4 = tk.Button(window, text="4", padx=20, pady=20, command=lambda:buttonClicked(4,True))
button_5 = tk.Button(window, text="5", padx=20, pady=20, command=lambda:buttonClicked(5,True))
button_6 = tk.Button(window, text="6", padx=20, pady=20, command=lambda:buttonClicked(6,True))
button_7 = tk.Button(window, text="7", padx=20, pady=20, command=lambda:buttonClicked(7,True))
button_8 = tk.Button(window, text="8", padx=20, pady=20, command=lambda:buttonClicked(8,True))
button_9 = tk.Button(window, text="9", padx=20, pady=20, command=lambda:buttonClicked(9,True))
button_division = tk.Button(window, text="÷", padx=20, pady=20, command=lambda:buttonClicked("/",False))
button_multiplicacion = tk.Button(window, text="×", padx=20, pady=20, command=lambda:buttonClicked("*",False))
button_resta = tk.Button(window, text="-", padx=20, pady=20, command=lambda:buttonClicked("-",False))
button_suma = tk.Button(window, text="+", padx=20, pady=20, command=lambda:buttonClicked("+",False))
button_decimal = tk.Button(window, text=",", padx=20, pady=20, command=lambda:buttonClicked(".",False))
button_igual = tk.Button(window, text="=", padx=20, pady=20, command=lambda:buttonClicked("=",False))

label.grid(row=0, columnspan=3, sticky="nsew")
button_clear.grid(row=0, column=3, sticky="nsew")
button_0.grid(row=4, column=0, sticky="nsew")
button_1.grid(row=3, column=0, sticky="nsew")
button_2.grid(row=3, column=1, sticky="nsew")
button_3.grid(row=3, column=2, sticky="nsew")
button_4.grid(row=2, column=0, sticky="nsew")
button_5.grid(row=2, column=1, sticky="nsew")
button_6.grid(row=2, column=2, sticky="nsew")
button_7.grid(row=1, column=0, sticky="nsew")
button_8.grid(row=1, column=1, sticky="nsew")
button_9.grid(row=1, column=2, sticky="nsew")
button_division.grid(row=1, column=3, sticky="nsew")
button_multiplicacion.grid(row=2, column=3, sticky="nsew")
button_resta.grid(row=3, column=3, sticky="nsew")
button_suma.grid(row=4, column=3, sticky="nsew")
button_decimal.grid(row=4, column=1, sticky="nsew")
button_igual.grid(row=4, column=2, sticky="nsew")

window.mainloop()