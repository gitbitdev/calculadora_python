import tkinter as tk

window = tk.Tk()
window.title("Calculadora")
button_0 = tk.Button(window, text="0", padx=20, pady=20)
button_1 = tk.Button(window, text="1", padx=20, pady=20)
button_2 = tk.Button(window, text="2", padx=20, pady=20)
button_3 = tk.Button(window, text="3", padx=20, pady=20)
button_4 = tk.Button(window, text="4", padx=20, pady=20)
button_5 = tk.Button(window, text="5", padx=20, pady=20)
button_6 = tk.Button(window, text="6", padx=20, pady=20)
button_7 = tk.Button(window, text="7", padx=20, pady=20)
button_8 = tk.Button(window, text="8", padx=20, pady=20)
button_9 = tk.Button(window, text="9", padx=20, pady=20)
button_division = tk.Button(window, text="÷", padx=20, pady=20)
button_multiplicacion = tk.Button(window, text="×", padx=20, pady=20)
button_resta = tk.Button(window, text="-", padx=20, pady=20)
button_suma = tk.Button(window, text="+", padx=20, pady=20)
button_decimal = tk.Button(window, text=",", padx=20, pady=20)
button_igual = tk.Button(window, text="=", padx=20, pady=20)

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