import random

rock = "Rock"
scissors = "Scissors"
paper = "Paper"

player_choose = input("For exit of the program write 'end'."
                      " For planing choose [r] for Rock, [s] for Scissors, [p] for Paper: ")
while player_choose != "end":
    if player_choose == "r":
        player_choose = rock
    elif player_choose == "s":
        player_choose = scissors
    elif player_choose == "p":
        player_choose = paper
    else:
        print("Please try agen...")
        player_choose = input("Choose [r] Rock, [s] Scissors, [p] Paper: ")
        continue
        # raise SystemError("Invalid option! Please try agen...")
    computer_random_number = random.randint(1, 3)

    computers_movement = ""

    if computer_random_number == 1:
        computers_movement = rock
    elif computer_random_number == 2:
        computers_movement = scissors
    else:
        computers_movement = paper

    print(f"Computer choose: {computers_movement}")

    if (player_choose == rock and computers_movement == scissors) \
            or (player_choose == scissors and computers_movement == paper) \
            or (player_choose == paper and computers_movement == rock):
        print("You win!")
    elif (player_choose == rock and computers_movement == paper) \
            or (player_choose == scissors and computers_movement == rock) \
            or (player_choose == paper and computers_movement == scissors):
        print("You lose :(")
    else:
        print("Draw")
    player_choose = input("Choose [r] Rock, [s] Scissors, [p] Paper: ")

