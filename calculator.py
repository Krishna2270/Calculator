import tkinter as tk
from tkinter import messagebox

def press(key):
    entry.insert(tk.END, key)

def calculate():
    try:
        expr = entry.get()
        response = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(tk.END, response)
    except Exception:
        messagebox.showerror("Error", " Invalid Expression")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")
root.geometry('360x450')
root.resizable(0, 0)

entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                  bg="#4CAF50", fg="white", command=calculate). grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                  command=lambda t=text: press(t)).grid(row=row, column=col, padx=5, pady=5)

tk.Button(root, text="C", width=23, height=2, font=("Arial", 14),
          bg="#f44336", fg="White", command=clear).grid(row=5, column=0, columnspan=4, padx=5, pady=5)
root.mainloop()
