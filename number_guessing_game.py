import tkinter as tk
from tkinter import messagebox
import random

# Generate random number
secret_number = random.randint(1, 100)
attempts = 0


def check_guess():
    global attempts

    try:
        guess = int(entry_guess.get())
        attempts += 1

        if guess < secret_number:
            result_label.config(
                text="Too Low! Try Again.", fg="red")
        elif guess > secret_number:
            result_label.config(
                text="Too High! Try Again.", fg="red")
        else:
            result_label.config(
                text=f"🎉 Correct! You guessed it in {attempts} attempts.",
                fg="green")
            messagebox.showinfo(
                "Congratulations!",
                f"You guessed the number in {attempts} attempts!"
            )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number!"
        )


def reset_game():
    global secret_number, attempts

    secret_number = random.randint(1, 100)
    attempts = 0

    entry_guess.delete(0, tk.END)
    result_label.config(text="")
    messagebox.showinfo(
        "New Game",
        "A new number has been generated!"
    )


# Main Window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.resizable(False, False)

# Heading
title_label = tk.Label(
    root,
    text="🎯 Number Guessing Game",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=15)

# Instructions
instruction_label = tk.Label(
    root,
    text="Guess a number between 1 and 100",
    font=("Arial", 12)
)
instruction_label.pack()

# Input Box
entry_guess = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center"
)
entry_guess.pack(pady=15)

# Guess Button
guess_button = tk.Button(
    root,
    text="Check Guess",
    font=("Arial", 12),
    command=check_guess
)
guess_button.pack(pady=5)

# Reset Button
reset_button = tk.Button(
    root,
    text="New Game",
    font=("Arial", 12),
    command=reset_game
)
reset_button.pack(pady=5)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold")
)
result_label.pack(pady=20)

# Run Application
root.mainloop()