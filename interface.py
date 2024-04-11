import tkinter as tk
from tkinter import messagebox
import random
from roll_dice import roll_dice

class Interface:
    def __init__(self, master):
        self.master = master
        master.title("Dice Roller")

        self.frame = tk.Frame(master)
        self.frame.pack(padx=40, pady=40)

        self.sides_label = tk.Label(self.frame, text="Number of sides:")
        self.sides_label.grid(row=0, column=0, sticky="w")

        self.sides_entry = tk.Entry(self.frame)
        self.sides_entry.grid(row=0, column=1)

        self.rolls_label = tk.Label(self.frame, text="Number of rolls:")
        self.rolls_label.grid(row=1, column=0, sticky="w")

        self.rolls_entry = tk.Entry(self.frame)
        self.rolls_entry.grid(row=1, column=1)

        self.advantage_var = tk.BooleanVar()
        self.advantage_checkbutton = tk.Checkbutton(self.frame, text="Advantage", variable=self.advantage_var)
        self.advantage_checkbutton.grid(row=2, column=0, sticky="w")

        self.disadvantage_var = tk.BooleanVar()
        self.disadvantage_checkbutton = tk.Checkbutton(self.frame, text="Disadvantage", variable=self.disadvantage_var)
        self.disadvantage_checkbutton.grid(row=3, column=0, sticky="w")

        self.roll_button = tk.Button(self.frame, text="Roll Dice", command=self.roll_dice)
        self.roll_button.grid(row=4, columnspan=2, pady=15)

        self.result_text = tk.Text(self.frame, height=5, width=55)
        self.result_text.grid(row=5, columnspan=2, pady=15)
        
    def roll_dice(self):
        sides = int(self.sides_entry.get())
        rolls = int(self.rolls_entry.get())
        advantage = self.advantage_var.get()
        disadvantage = self.disadvantage_var.get()

        self.result_text.delete("1.0", tk.END)
        results = roll_dice(sides, rolls, advantage, disadvantage)
        for result in results:
            self.result_text.insert(tk.END, f"You rolled: {result}\n")
