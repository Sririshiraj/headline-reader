import tkinter as tk
from tkinter import messagebox


class CalculatorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Calculator App")
        self.root.geometry("350x450")
        self.root.resizable(False, False)

        self.expression = ""

        self.create_widgets()

    def create_widgets(self):
        # Display
        self.entry = tk.Entry(
            self.root,
            font=("Arial", 22),
            bd=10,
            relief=tk.RIDGE,
            justify="right"
        )
        self.entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack()

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        row = 0
        col = 0

        for text in buttons:
            if text == "=":
                button = tk.Button(
                    buttons_frame,
                    text=text,
                    font=("Arial", 16),
                    width=5,
                    height=2,
                    bg="green",
                    fg="white",
                    command=self.calculate
                )
            else:
                button = tk.Button(
                    buttons_frame,
                    text=text,
                    font=("Arial", 16),
                    width=5,
                    height=2,
                    command=lambda t=text: self.add_to_expression(t)
                )

            button.grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col > 3:
                col = 0
                row += 1

        # Clear button
        clear_button = tk.Button(
            self.root,
            text="Clear",
            font=("Arial", 16),
            bg="red",
            fg="white",
            command=self.clear
        )
        clear_button.pack(fill=tk.BOTH, padx=10, pady=5)

    def add_to_expression(self, value):
        self.expression += value
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
            self.expression = result
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            self.clear()

    def clear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
