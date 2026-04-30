# Name : Shreyas Rajendra Shigwan, Roll no. : 90 , CSE(AIML)-B
# Project : A Simple Calculator and Converter using tkinter library
import tkinter as tk
from tkinter import messagebox

TITLE_FONT = ("Arial", 14, "bold")
TEXT_FONT = ("Arial", 12)
ENTRY_FONT = ("Arial", 14)

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def show_calculator():
    clear_frame(main_frame)
    tk.Label(main_frame, text="Calculator", font=TITLE_FONT).pack(pady=(0, 12))

    entry = tk.Entry(main_frame, width=28, font=ENTRY_FONT, bd=3, relief="sunken")
    entry.pack(pady=5)

    def insert_text(value):
        if value == "C":
            entry.delete(0, tk.END)
        else:
            entry.insert(tk.END, value)

    def calculate():
        expression = entry.get().split("=")[0]
        try:
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, f"{expression} = {result}")
        except Exception:
            messagebox.showerror("Error", "Invalid expression")

    button_frame = tk.Frame(main_frame)
    button_frame.pack(pady=10)

    buttons = [
        "7", "8", "9", "+",
        "4", "5", "6", "-",
        "1", "2", "3", "*",
        "C", "0", ".", "/"
    ]
    for index, text in enumerate(buttons):
        tk.Button(
            button_frame,
            text=text,
            width=5,
            font=TEXT_FONT,
            command=lambda value=text: insert_text(value)
        ).grid(row=index // 4, column=index % 4, padx=4, pady=4)

    tk.Button(
        main_frame,
        text="Calculate",
        width=22,
        font=TEXT_FONT,
        command=calculate
    ).pack(pady=8)

def show_converter():
    clear_frame(main_frame)
    tk.Label(main_frame, text="Converter", font=TITLE_FONT).pack(pady=(0, 12))

    converters = [
        ("Mass (kg → g)", "g", lambda v: v * 1000),
        ("Temp (°C → °F)", "°F", lambda v: v * 9 / 5 + 32),
        ("Height (ft → cm)", "cm", lambda v: v * 30.48)
    ]

    for label_text, unit_label, func in converters:
        row = tk.Frame(main_frame)
        row.pack(fill="x", pady=6)

        tk.Label(row, text=label_text + ":", font=TEXT_FONT).pack(side=tk.LEFT)
        entry = tk.Entry(row, width=10, font=TEXT_FONT)
        entry.pack(side=tk.LEFT, padx=6)

        result_label = tk.Label(row, text="", font=TEXT_FONT, width=14, anchor="w")
        result_label.pack(side=tk.LEFT, padx=4)

        def convert(entry=entry, result_label=result_label, converter=func, unit=unit_label):
            try:
                value = float(entry.get())
                result_label.config(text=f"{converter(value):.2f} {unit}")
            except ValueError:
                messagebox.showerror("Error", "Invalid input")

        tk.Button(row, text="Go", font=TEXT_FONT, command=convert).pack(side=tk.LEFT)

root = tk.Tk()
root.title("Calculator & Converter")
root.geometry("360x420")
root.resizable(False, False)

top_frame = tk.Frame(root, pady=10)
top_frame.pack()

tk.Button(top_frame, text="Calculator", width=14, font=TEXT_FONT, command=show_calculator).pack(side=tk.LEFT, padx=8)
tk.Button(top_frame, text="Converter", width=14, font=TEXT_FONT, command=show_converter).pack(side=tk.LEFT, padx=8)

main_frame = tk.Frame(root, padx=10, pady=8)
main_frame.pack(fill="both", expand=True)

footer = tk.Label(root, text="Code by Shreyas Shigwan", fg="blue", font=("Arial", 9))
footer.pack(side=tk.BOTTOM, pady=8)

show_calculator()
root.mainloop()
