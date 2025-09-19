import random

# Use a dictionary for easier lookup of both names and values
choices = {"stone": -1, "paper": 0, "scissor": 1}
# Create a reverse mapping to get the name from the number
# {v: k for k, v in my_map.items()} is a common Python idiom for this
value_to_name = {v: k for k, v in choices.items()}

# --- Game Loop ---
while True:
    # --- Get User Input ---
    user_input = input("Enter your choice (stone, paper, scissor) or 'q' to quit: ").lower()

    if user_input == 'q':
        print("Thanks for playing!")
        break # Exit the loop

    if user_input not in choices:
        print("Invalid input. Please try again.")
        continue # Skip the rest of this iteration and ask again

    # --- Game Logic ---
    you = choices[user_input]
    computer = random.choice(list(choices.values()))

    print(f"\nYou chose: {value_to_name[you]}")
    print(f"Computer chose: {value_to_name[computer]}\n")

    # --- Simplified Win/Loss/Draw Conditions ---
    if computer == you:
        print("It's a draw! 🤝")
    # This single condition covers all three winning scenarios for the user:
    # 0 > -1 (paper > stone)
    # 1 > 0  (scissor > paper)
    # -1 > 1 (stone > scissor, which is the wrap-around case)
    elif (you == 0 and computer == -1) or \
         (you == 1 and computer == 0) or \
         (you == -1 and computer == 1):
        print("You won! 🎉")
    else:
        print("The computer won. 🤖")

    print("-" * 20) # Separator for the next round