import random

def game_win(computer, player):
    if computer == player:
        return None
    elif computer == "snake":
        if player == "water":
            return False
        elif player == "gun":
            return True
    elif computer == "water":
        if player == "gun":
            return False
        elif player == "snake":
            return True
    elif computer == "gun":
        if player == "snake":
            return False
        elif player == "water":
            return True

print("Snake 🐍 Water 💧 Gun 🔫 Game")
print("Choose one: snake, water, gun")

# Computer’s choice
computer_choice = random.choice(["snake", "water", "gun"])

# Player’s choice
player_choice = input("Your turn: ").lower()

print(f"Computer chose: {computer_choice}")
print(f"You chose: {player_choice}")

# Decide winner
result = game_win(computer_choice, player_choice)

if result is None:
    print("It's a tie!")
elif result:
    print("You win! 🎉")
else:
    print("You lose! 😢")
