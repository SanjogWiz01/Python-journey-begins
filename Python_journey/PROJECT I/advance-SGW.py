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

print("\n===== Snake 🐍 Water 💧 Gun 🔫 Game =====\n")
rounds = int(input("How many rounds you want to play? "))

player_score = 0
computer_score = 0

for i in range(1, rounds + 1):
    print(f"\n--- Round {i} ---")
    computer_choice = random.choice(["snake", "water", "gun"])
    player_choice = input("Choose (snake / water / gun): ").lower()

    if player_choice not in ["snake", "water", "gun"]:
        print("❌ Invalid choice, you lost this round!")
        computer_score += 1
        continue

    print(f"👉 Computer chose: {computer_choice}")
    print(f"👉 You chose: {player_choice}")

    result = game_win(computer_choice, player_choice)

    if result is None:
        print("😐 It's a tie this round.")
    elif result:
        print("🎉 You win this round!")
        player_score += 1
    else:
        print("😢 You lose this round!")
        computer_score += 1

    print(f"Score: You {player_score} - {computer_score} Computer")

print("\n===== Final Result =====")
if player_score > computer_score:
    print(f"🏆 Congratulations! You won the match {player_score} - {computer_score}")
elif player_score < computer_score:
    print(f"💻 Computer wins the match {computer_score} - {player_score}. Better luck next time!")
else:
    print(f"🤝 It's a draw! Final Score: {player_score} - {computer_score}")
print("Thanks for playing! 😊")