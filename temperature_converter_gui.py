import tkinter as tk
from tkinter import messagebox

# Function: Celsius → Fahrenheit
def c_to_f():
    try:
        c = float(entry_temp.get())
        f = (c * 9/5) + 32
        result_label.config(text=f"Fahrenheit: {f:.2f} °F")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")

# Function: Fahrenheit → Celsius
def f_to_c():
    try:
        f = float(entry_temp.get())
        c = (f - 32) * 5/9
        result_label.config(text=f"Celsius: {c:.2f} °C")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")

# Create window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x250")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Temperature Converter",
                       font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Input field
entry_temp = tk.Entry(root, font=("Arial", 14), justify="center")
entry_temp.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Buttons
btn_c_to_f = tk.Button(button_frame,
                       text="Celsius → Fahrenheit",
                       command=c_to_f,
                       width=18,
                       bg="lightblue")

btn_c_to_f.grid(row=0, column=0, padx=5)

btn_f_to_c = tk.Button(button_frame,
                       text="Fahrenheit → Celsius",
                       command=f_to_c,
                       width=18,
                       bg="lightgreen")

btn_f_to_c.grid(row=0, column=1, padx=5)

# Result Label
result_label = tk.Label(root, text="Result will appear here",
                        font=("Arial", 12))
result_label.pack(pady=20)

# Run app
root.mainloop()