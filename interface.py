import tkinter as tk
from tkinter import ttk
import random

def roll_dice(sides, rolls, advantage=False, disadvantage=False):
    results = []

    for _ in range(rolls):
        if advantage:
            roll1 = random.randint(1, sides)
            roll2 = random.randint(1, sides)
            result = max(roll1, roll2)
            results.append((result, roll1, roll2, "Advantage"))
        elif disadvantage:
            roll1 = random.randint(1, sides)
            roll2 = random.randint(1, sides)
            result = min(roll1, roll2)
            results.append((result, roll1, roll2, "Disadvantage"))
        else:
            result = random.randint(1, sides)
            results.append((result, None, None, "Standard"))

    return results

class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dice Roller")
        self.setup_ui()

    def setup_ui(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(padx=10, pady=10)

        self.create_standard_roll_tab()
        self.create_advantage_roll_tab()
        self.create_disadvantage_roll_tab()

    def create_standard_roll_tab(self):
        standard_roll_tab = ttk.Frame(self.notebook)
        self.notebook.add(standard_roll_tab, text="Standard Roll")

        self.create_roll_options(standard_roll_tab)

    def create_advantage_roll_tab(self):
        advantage_roll_tab = ttk.Frame(self.notebook)
        self.notebook.add(advantage_roll_tab, text="Advantage Roll")

        self.create_roll_options(advantage_roll_tab)

    def create_disadvantage_roll_tab(self):
        disadvantage_roll_tab = ttk.Frame(self.notebook)
        self.notebook.add(disadvantage_roll_tab, text="Disadvantage Roll")

        self.create_roll_options(disadvantage_roll_tab)

    def create_roll_options(self, frame):
        sides_label = tk.Label(frame, text="Number of sides:")
        sides_label.grid(row=0, column=0, sticky="w")

        sides_var = tk.StringVar()
        sides_options = [4, 6, 8, 10, 12, 20]  # Example sides options
        sides_var.set(sides_options[0])  # Default to the first option
        sides_menu = tk.OptionMenu(frame, sides_var, *sides_options)
        sides_menu.grid(row=0, column=1, sticky="ew")

        rolls_label = tk.Label(frame, text="Number of rolls:")
        rolls_label.grid(row=1, column=0, sticky="w")

        rolls_var = tk.StringVar()
        rolls_options = [1, 2, 3, 4, 5]  # Example rolls options
        rolls_var.set(rolls_options[0])  # Default to the first option
        rolls_menu = tk.OptionMenu(frame, rolls_var, *rolls_options)
        rolls_menu.grid(row=1, column=1, sticky="ew")

        roll_button = tk.Button(frame, text="Roll Dice", command=lambda: self.roll_dice(frame, sides_var, rolls_var))
        roll_button.grid(row=2, columnspan=2, pady=5)

        result_text = tk.Text(frame, height=5, width=40)
        result_text.grid(row=3, columnspan=2, pady=5)
        frame.result_text = result_text  # Store a reference to the result text widget in the frame

    def roll_dice(self, frame, sides_var, rolls_var):
        sides = int(sides_var.get())
        rolls = int(rolls_var.get())

        result_text = frame.result_text  # Get the reference to the result text widget
        result_text.delete("1.0", tk.END)

        if frame.master.tab("current")["text"] == "Advantage Roll":
            results = roll_dice(sides, rolls, advantage=True)
        elif frame.master.tab("current")["text"] == "Disadvantage Roll":
            results = roll_dice(sides, rolls, disadvantage=True)
        else:
            results = roll_dice(sides, rolls)

        for result in results:
            if result[3] == "Standard":
                result_text.insert(tk.END, f"You rolled: {result[0]}\n")
            else:
                result_text.insert(tk.END, f"You rolled with {result[3]}: {result[1]} and {result[2]}\nChosen roll: {result[0]}\n")

app = Interface()
app.geometry("450x300")
app.mainloop()
