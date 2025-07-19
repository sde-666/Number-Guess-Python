import tkinter as tk
from tkinter import messagebox
import random

# Global variables
number_to_guess = 0
attempts = 0
max_attempts = 5

# Functions
def start_new_game():
    global number_to_guess, attempts
    number_to_guess = random.randint(1, 30)
    attempts = 0
    entry.config(state="normal")
    guess_button.config(state="normal")
    result_label.config(text="")
    entry.delete(0, tk.END)
    title_label.config(text="Guess the number between 1 and 30")
    play_again_button.pack_forget()

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number.")
        return

    if not 1 <= guess <= 30:
        result_label.config(text="Out of range! Enter a number from 1 to 30.", fg="red")
        return

    attempts += 1

    if guess == number_to_guess:
        result_label.config(text=f"Correct! You guessed it in {attempts} attempts.", fg="green")
        title_label.config(text="Congratulations!")
        entry.config(state="disabled")
        guess_button.config(state="disabled")
        play_again_button.pack(pady=10)
    elif attempts >= max_attempts:
        result_label.config(text=f"Game Over. The number was {number_to_guess}.", fg="red")
        title_label.config(text="Better luck next time.")
        entry.config(state="disabled")
        guess_button.config(state="disabled")
        play_again_button.pack(pady=10)
    elif guess < number_to_guess:
        result_label.config(text="Too low! Try again.", fg="blue")
    else:
        result_label.config(text="Too high! Try again.", fg="purple")

# GUI setup
root = tk.Tk()
root.title("Number Guessing Game")

title_label = tk.Label(root, text="Guess the number between 1 and 30", font=("Arial", 14))
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

guess_button = tk.Button(root, text="Guess", font=("Arial", 12), command=check_guess)
guess_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

play_again_button = tk.Button(root, text="Play Again", font=("Arial", 12), command=start_new_game)
play_again_button.pack(pady=5)
play_again_button.pack_forget()  # initially hidden

# Start game
start_new_game()
root.mainloop()
