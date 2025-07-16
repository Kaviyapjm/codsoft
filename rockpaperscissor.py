import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def decide_winner(user, computer):
    outcomes = {
        'rock': {'scissors': 'win', 'paper': 'lose'},
        'paper': {'rock': 'win', 'scissors': 'lose'},
        'scissors': {'paper': 'win', 'rock': 'lose'}
    }
    if user == computer:
        return 'tie'
    return outcomes[user][computer]

def display_result(user, computer, result):
    print(f"\n🧑 You chose: {user}")
    print(f"🤖 Computer chose: {computer}")
    if result == 'win':
        print("🎉 You win this round!")
    elif result == 'lose':
        print("💥 You lost this round!")
    else:
        print("😐 It's a tie!")

def valid_choice(choice):
    return choice in ['rock', 'paper', 'scissors']

def play_game():
    user_score = 0
    computer_score = 0
    round_no = 1

    print("Welcome to Rock-Paper-Scissors Game 🎮")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'exit' anytime to quit.\n")

    while True:
        print(f"--- Round {round_no} ---")
        user_input = input("Your move: ").strip().lower()

        if user_input == 'exit':
            print("\n👋 Exiting game. Final Score:")
            print(f"🧑 You: {user_score} | 🤖 Computer: {computer_score}")
            break

        if not valid_choice(user_input):
            print("⚠️ Invalid choice. Try again.\n")
            continue

        computer_input = get_computer_choice()
        result = decide_winner(user_input, computer_input)
        display_result(user_input, computer_input, result)

        if result == 'win':
            user_score += 1
        elif result == 'lose':
            computer_score += 1

        print(f"Score ➤ You: {user_score} | Computer: {computer_score}\n")
        round_no += 1

if __name__ == "__main__":
    play_game()
