import random
from Dices import rollD6, rollD4

# Number of wins needed to win the game:
winning_score = 5

# Arrays for storing player names, wins, and roll history
player_names = []
player_wins = []
player_roll_history = []


# Obtain the number of players:
number_of_players = int(input("How many players will play? "))

# For loop to obtain the player names:
for i in range(number_of_players):
    name = input(f" Enter your name: ")
    player_names.append(name)


# Initialze scores and roll history
for i in range(number_of_players):
    player_wins.append(0)
    player_roll_history.append([])

print(f"\n Welcome to the cooler mutliplayer battle of dices🎲🎲")


# Gameover loop
gameover = False
rounds = 0

while not gameover:
    print(f"\n=== Round {rounds+1} ===")

# Dice roll for each player in the current round:
    current_rolls = []


# Roll the dice for each player:
    for i in range(number_of_players):
        roll = rollD4() + rollD6()
        current_rolls.append(roll)
        player_roll_history[i].append(roll)
        print(f"{player_names[i]} rolled {roll}")

    input("\nPress Enter to continue...")

# ... still in the while gameover is False:

# Obtain the highest roll this round:
    max_roll = max(current_rolls)

# Winners will store information about who won this round:
    winners = []

# Search for all players who got the highest roll:
    for j in range(len(current_rolls)):
        if current_rolls[j] == max_roll:
            winners.append(player_names[j])
            player_wins[j] += 1

    print(f"Winners of this round are {', '.join(winners)}")

# ... still in the while gameover is False:

# Check if someone reached winning score
#( It is unlikely but there might be more than one winner)
    for z in range(number_of_players):
        if player_wins[z] >= winning_score:
            print(f"\n {player_names[z]} is the newest battle of dices champion🏆!")
            gameover = True

    if not gameover:
        print(" The battle is still going...🔥")

   
    rounds += 1


filename = input("\nEnter the filename to save the results: ")
with open(filename, "w") as file:
    for round_number in range(rounds):
        file.write(f"Round {round_number+1}: ")
        rolls_str = ""
        for i in range(number_of_players):
            rolls_str += f"{player_names[i]} rolled {player_roll_history[i][round_number]}"
            if i < number_of_players - 1:
                rolls_str += ", "
        print(f"saving {rolls_str}")
        file.write(rolls_str + "\n")

print(f"Results saved in {filename}")
