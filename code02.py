import tkinter as tk
from tkinter import messagebox

TITLE_FONT, TEXT_FONT, ENTRY_FONT = ("Arial", 14, "bold"), ("Arial", 12), ("Arial", 14)

def calculate():
    try:
        expr = entry.get().split("=")[0]
        res = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"{expr} = {res}")
    except:
        messagebox.showerror("Error", "Invalid expression")

def press(val):
    if val == "C": entry.delete(0, tk.END)
    else: entry.insert(tk.END, val)

root = tk.Tk()
root.title("Calculator")
root.geometry("360x400")

tk.Label(root, text="Calculator", font=TITLE_FONT).pack(pady=10)
entry = tk.Entry(root, width=25, font=ENTRY_FONT, bd=3, relief="sunken")
entry.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

btns = ["7","8","9","+","4","5","6","-","1","2","3","*","C","0",".","/"]
for i, txt in enumerate(btns):
    tk.Button(btn_frame, text=txt, width=5, font=TEXT_FONT, 
              command=lambda t=txt: press(t)).grid(row=i//4, column=i%4, padx=4, pady=4)

tk.Button(root, text="Calculate", width=22, font=TEXT_FONT, command=calculate).pack(pady=10)
tk.Label(root, text="Code by Shreyas Shigwan", fg="blue", font=("Arial", 9)).pack(side=tk.BOTTOM, pady=10)

root.mainloop()
