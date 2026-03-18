import tkinter as tk

root = tk.Tk()
root.title("My Calculator")
root.geometry("320x450")
root.configure(bg="#1e1e1e")

entry = tk.Entry(root, width=18, font=("Arial", 24), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

def click(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

btn_style = {
    "font": ("Arial", 14),
    "width": 5,
    "height": 2,
    "fg": "white"
}

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)
]

for (text, row, col) in buttons:
    if text == "C":
        btn = tk.Button(root, text=text, command=clear, bg="#ff4d4d", **btn_style)
    elif text == "=":
        btn = tk.Button(root, text=text, command=calculate, bg="#4CAF50", **btn_style)
    elif text in "+-*/":
        btn = tk.Button(root, text=text, command=lambda t=text: click(t), bg="#ff9500", **btn_style)
    else:
        btn = tk.Button(root, text=text, command=lambda t=text: click(t), bg="#333", **btn_style)
    
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()