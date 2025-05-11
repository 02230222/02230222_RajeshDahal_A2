import random
from RajeshDahal_02230222_A2_PB import pokemon_card_binder_manager  # ✅ Linking Part B

scores = {
    "guess_number": 0,
    "rps": 0,
    "trivia": 0
}

def input_int(prompt, min_val=None, max_val=None):
    """Prompt user for an integer input with optional range validation."""
    while True:
        try:
            val = int(input(prompt))
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                raise ValueError()
            return val
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def guess_number_game():
    """Guess a random number between 1 and 10."""
    print("\n--- Guess the Number Game ---")
    secret = random.randint(1, 10)
    attempts = 0
    while True:
        guess = input_int("Guess a number between 1 and 10: ", 1, 10)
        attempts += 1
        if guess == secret:
            print("Correct!")
            break
        else:
            print("Wrong guess. Try again.")
    score = max(0, 10 - attempts)
    print(f"You guessed it in {attempts} attempts. Score: {score}")
    scores["guess_number"] += score

def rock_paper_scissors_game():
    """Play a few rounds of Rock, Paper, Scissors."""
    print("\n--- Rock Paper Scissors ---")
    options = ['rock', 'paper', 'scissors']
    wins = 0
    rounds = input_int("How many rounds do you want to play? ", 1)
    for _ in range(rounds):
        user = input("Choose rock, paper or scissors: ").lower()
        if user not in options:
            print("Invalid choice.")
            continue
        computer = random.choice(options)
        print(f"Computer chose {computer}.")
        if user == computer:
            print("It's a tie.")
        elif (user == "rock" and computer == "scissors") or \
             (user == "scissors" and computer == "paper") or \
             (user == "paper" and computer == "rock"):
            print("You win!")
            wins += 1
        else:
            print("You lose.")
    print(f"Total wins: {wins}")
    scores["rps"] += wins

def trivia_quiz_game():
    """Answer multiple-choice trivia questions."""
    print("\n--- Trivia Pursuit ---")
    questions = {
        "Science": [
            ("What planet is known as the Red Planet?", ["Mars", "Earth", "Venus", "Jupiter"], "Mars"),
            ("What gas do plants absorb from the atmosphere?", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "Carbon Dioxide")
        ],
        "History": [
            ("Who was the first president of the United States?", ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"], "George Washington"),
            ("In which year did World War II end?", ["1945", "1942", "1939", "1918"], "1945")
        ]
    }
    score = 0
    for category, qs in questions.items():
        print(f"\nCategory: {category}")
        for q, options, correct in qs:
            print(q)
            for idx, opt in enumerate(options):
                print(f"{idx + 1}. {opt}")
            choice = input_int("Your answer (1-4): ", 1, 4)
            if options[choice - 1] == correct:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong. Correct answer: {correct}")
    print(f"Trivia Score: {score}")
    scores["trivia"] += score

def check_overall_score():
    """Display scores from all games played."""
    print("\n--- Overall Score ---")
    print(f"Guess Number Game Score: {scores['guess_number']}")
    print(f"Rock Paper Scissors Score: {scores['rps']}")
    print(f"Trivia Quiz Score: {scores['trivia']}")
    total = scores['guess_number'] + scores['rps'] + scores['trivia']
    print(f"Total Score: {total}")

def main():
    """Main loop to select and play different games."""
    while True:
        print("\nSelect a function (0-5):")
        print("1. Guess Number game")
        print("2. Rock paper scissors game")
        print("3. Trivia Pursuit Game")
        print("4. Pokemon Card Binder Manager")
        print("5. Check Current Overall score")
        print("0. Exit program")
        choice = input_int("Enter your choice: ", 0, 5)

        if choice == 1:
            guess_number_game()
        elif choice == 2:
            rock_paper_scissors_game()
        elif choice == 3:
            trivia_quiz_game()
        elif choice == 4:
            pokemon_card_binder_manager()  # ✅ Calls the external Part B game
        elif choice == 5:
            check_overall_score()
        elif choice == 0:
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
