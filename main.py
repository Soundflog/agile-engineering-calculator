import tkinter as tk
from tkinter import font
from math import sin, cos, tan, log, sqrt, factorial, radians, degrees, asin, acos, atan, exp


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Инженерный Калькулятор")

        self.entry = tk.Entry(root, width=40, borderwidth=3, font=("Arial", 14))
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('sqrt', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('log', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('^', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('(', 5, 3), (')', 5, 4),
            ('fact', 6, 0), ('rads', 6, 1), ('degs', 6, 2), ('asin', 6, 3), ('acos', 6, 4),
            ('atan', 7, 0), ('exp', 7, 1)
        ]

        for (text, row, col) in buttons:
            if text.isdigit() or text == '.':
                button_style = {"relief": "raised", "bg": "#f0f0f0"}
            else:
                button_style = {"relief": "groove", "bg": "#f0f0f0"}

            button = tk.Button(
                self.root, text=text, width=7, height=2, font=("Arial", 14),
                fg="#000000", activebackground="#d3d3d3", borderwidth=1,
                command=lambda t=text: self.on_button_click(t), **button_style
            )
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

            # Apply hover effect for all buttons
            button.bind("<Enter>", lambda e, b=button: b.configure(bg="#e0e0e0"))
            button.bind("<Leave>", lambda e, b=button: b.configure(bg=button_style["bg"]))

    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                expression = self.entry.get()
                result = eval(self.replace_functions(expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, char)

    def replace_functions(self, expression):
        return expression.replace('sin', 'sin').replace('cos', 'cos').replace('tan', 'tan') \
            .replace('log', 'log').replace('sqrt', 'sqrt').replace('^', '**') \
            .replace('fact', 'factorial').replace('rads', 'radians').replace('degs', 'degrees') \
            .replace('asin', 'asin').replace('acos', 'acos').replace('atan', 'atan').replace('exp', 'exp')


if __name__ == "__main__":
    root = tk.Tk()

    # Apply styles for a cleaner look
    for i in range(8):
        root.grid_rowconfigure(i, weight=1)
    for j in range(5):
        root.grid_columnconfigure(j, weight=1)

    app = CalculatorApp(root)
    root.mainloop()
