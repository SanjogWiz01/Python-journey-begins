import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guess")
        self.root.geometry("500x350")
        self.root.resizable(False, False)

        # Initialize game variables
        self.target_number = random.randint(1, 200)
        self.attempts_left = 10

        # Title
        self.title_label = tk.Label(root, text="🎯 Number Guess", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=15)

        # Instructions
        self.instruction_label = tk.Label(
            root, 
            text="Guess a number between 1 and 200.\nYou have 10 chances!",
            font=("Arial", 12)
        )
        self.instruction_label.pack(pady=10)

        # Entry box
        self.entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.entry.pack(pady=5)

        # Submit button
        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess, font=("Arial", 12))
        self.submit_button.pack(pady=10)

        # Feedback
        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=5)

        # Attempts left
        self.attempts_label = tk.Label(root, text=f"Attempts left: {self.attempts_left}", font=("Arial", 12))
        self.attempts_label.pack(pady=5)

        # "Made by Wizard" in bottom-right
        self.signature_label = tk.Label(root, text="Made by Wizard", font=("Arial", 10, "italic"))
        self.signature_label.place(relx=1.0, rely=1.0, anchor="se")

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess < 1 or guess > 200:
                self.feedback_label.config(text="⚠️ Enter a number between 1 and 200!", fg="red")
                return
        except ValueError:
            self.feedback_label.config(text="⚠️ Only integers allowed!", fg="red")
            return

        self.attempts_left -= 1
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")

        if guess == self.target_number:
            messagebox.showinfo("Congratulations!", f"🎉 You guessed it! The number was {self.target_number}")
            self.reset_game()
        elif guess < self.target_number:
            self.feedback_label.config(text="📉 Too low! Try again.", fg="blue")
        else:
            self.feedback_label.config(text="📈 Too high! Try again.", fg="blue")

        if self.attempts_left == 0:
            messagebox.showinfo("Game Over", f"💻 Computer wins! The number was {self.target_number}")
            self.reset_game()

    def reset_game(self):
        self.target_number = random.randint(1, 200)
        self.attempts_left = 10
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
        self.feedback_label.config(text="")
        self.entry.delete(0, tk.END)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
