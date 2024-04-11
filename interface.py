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

        self.roll_button = tk.Button(self.frame, text="Roll Dice", command=self.roll_dice)
        self.roll_button.grid(row=2, columnspan=2, pady=15)

        self.result_text = tk.Text(self.frame, height=5, width=30)
        self.result_text.grid(row=3, columnspan=2, pady=15)

        self.quit_button = tk.Button(self.frame, text="Quit", command=self.quit_program)
        self.quit_button.grid(row=4, columnspan=2)
        
    def animate_roll(self):
        sides = int(self.sides_entry.get())
        rolls = int(self.rolls_entry.get())

        self.result_text.delete("1.0", tk.END)

        # Simulate rolling animation
        for _ in range(5):  # Change this value to control the number of animations
            dice_roll = random.randint(1, sides)
            self.result_text.insert(tk.END, f"Rolling: {dice_roll}\n")
            self.master.update()  # Force GUI update to display the rolling animation
            self.master.after(200)  # Control the speed of the animation
        self.result_text.delete("1.0", tk.END)

        # Display final results
        results = roll_dice(sides, rolls)
        for result in results:
            self.result_text.insert(tk.END, f"You rolled: {result}\n")

    def roll_dice(self):
        sides = int(self.sides_entry.get())
        rolls = int(self.rolls_entry.get())

        self.result_text.delete("1.0", tk.END)
        for _ in range(rolls):
            dice = random.randint(1, sides)
            self.result_text.insert(tk.END, f"You rolled: {dice}\n")

    def quit_program(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.master.destroy()
