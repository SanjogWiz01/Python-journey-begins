import tkinter as tk
import random
from PIL import Image, ImageTk

# Game choices
choices = ["rock", "paper", "scissors"]

# Winner logic
def get_winner(user, comp):
    if user == comp:
        return "😐 It's a Tie!"
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        return "🎉 You Win!"
    else:
        return "😢 You Lose!"

def play(user_choice):
    comp_choice = random.choice(choices)

    # Update images
    user_img_label.config(image=images[user_choice])
    comp_img_label.config(image=images[comp_choice])

    # Show winner
    result.set(get_winner(user_choice, comp_choice))

# GUI Setup
root = tk.Tk()
root.title("RPS Battle Arena")
root.geometry("700x500")
root.config(bg="white")

result = tk.StringVar()
result.set("Make your move!")

# Load images (JPG version)
images = {
    "rock": ImageTk.PhotoImage(Image.open("rock.jpg").resize((120, 120))),
    "paper": ImageTk.PhotoImage(Image.open("paper.jpg").resize((120, 120))),
    "scissors": ImageTk.PhotoImage(Image.open("s.jpg").resize((120, 120))),
}

# Labels for user & computer
tk.Label(root, text="👤 You", font=("Arial", 14), bg="white").place(x=150, y=50)
tk.Label(root, text="💻 Computer", font=("Arial", 14), bg="white").place(x=450, y=50)

user_img_label = tk.Label(root, bg="white")
user_img_label.place(x=120, y=100)

comp_img_label = tk.Label(root, bg="white")
comp_img_label.place(x=420, y=100)

# Buttons
tk.Button(root, image=images["rock"], command=lambda: play("rock")).place(x=120, y=300)
tk.Button(root, image=images["paper"], command=lambda: play("paper")).place(x=300, y=300)
tk.Button(root, image=images["scissors"], command=lambda: play("scissors")).place(x=480, y=300)

# Result Label
tk.Label(root, textvariable=result, font=("Arial", 18, "bold"), bg="red", fg="blue").pack(pady=20)

root.mainloop()
# def star(int x):