import tkinter as tk

window = tk.Tk()

window.title("Igloria")
window.geometry("400x300")
window.configure(bg="white")

label = tk.Label(window, text="Calculator", font=("arial",12))
label.pack(pady=10)

persnum = tk.Label(window, text="Enter your first number:", font=("arial",10))
persnum.pack()

entry = tk.Entry(window)
entry.pack()

sekannum = tk.Label(window, text="Enter your second number:", font=("arial",10))
sekannum.pack()

entry_1 = tk.Entry(window)
entry_1.pack()

result_label = tk.Label(window, text="Result: ", font=("arial",12))
result_label.pack(pady=10)

def add():
    num1 = float(entry.get())
    num2 = float(entry_1.get())
    result_label.config(text="Result: " + str(num1 + num2))

def subtract():
    num1 = float(entry.get())
    num2 = float(entry_1.get())
    result_label.config(text="Result: " + str(num1 - num2))

def multiply():
    num1 = float(entry.get())
    num2 = float(entry_1.get())
    result_label.config(text="Result: " + str(num1 * num2))

def divide():
    num1 = float(entry.get())
    num2 = float(entry_1.get())
    result_label.config(text="Result: " + str(num1 / num2))

btn_add = tk.Button(window, text="Add (+)", command=add)
btn_add.pack()

btn_sub = tk.Button(window, text="Subtract (-)", command=subtract)
btn_sub.pack()

btn_mul = tk.Button(window, text="Multiply (*)", command=multiply)
btn_mul.pack()

btn_div = tk.Button(window, text="Divide (/)", command=divide)
btn_div.pack()

window.mainloop()
