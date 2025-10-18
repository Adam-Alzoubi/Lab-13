from Dices import rollD6, rollD4
import copy


# Variable to keep track of the score:
rounds = 0
gameover = False

# Number of wins needed to win the game:
winning_score = 5

# Dictionary Template for storing player information:
player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []
}

#List to store the dicts for each player:
players=[]

print(f"\n Welcome to the cooler mutliplayer battle of dices🎲🎲")


# Obtain the number of players:
number_of_players = int(input("How many players will play? "))

# For loop to obtain the player names:
for i in range(number_of_players):

    #Make a deepcopy of the template for this player:
    player = copy.deepcopy(player_info)

    player["name"] = input(f"What is the name of player {i+1}? ")
    player["email"] = input(f"What is the e-mail of player {i+1}? ")
    player["country"] = input(f"What is the country of player {i+1}? ")

    players.append(player)

#Repeats until the game is over. As many rounds as neccessary:

while not gameover:
    print(f"\n=== Round {rounds+1} ===")

# Dice roll for each player in the current round:
    current_rolls = []

# Roll the dice for each player:
    for each_player in players:
        roll = rollD4() + rollD6()

        #player_rolls_history[i].append(roll)
        each_player["rolls"].append(roll)

        current_rolls.append(roll)

        print(f"player {each_player['name']} rolled {roll}")



# ... still in the while gameover is False:

# Obtain the highest roll this round:
    max_roll = max(current_rolls)

# Winners will store information about who won this round:
    winners = []

# Search for all players who got the highest roll:
for each_player in players:
    if (each_player["rolls"][-1]==max_roll):
        each_player["wins"] += 1
        print(f"player {each_player['name']} won in round {rounds}")

        winners.append(each_player['name'])

print(f"Winners of this round are {winners}")



# ... still in the while gameover is False:

# Check if someone reached winning score
for each_player in players:
    if (each_player['wins']>=winning_score):
        print(f"\n {each_player['name']} is the newest and coolest Batlle of Dices Champion!")
        gameover = True
if gameover is False:
         print(" The battle is still going on...🔥...Who will win in the end?")

rounds += 1

#Save results to a file 
filename = input("\nEnter the filename to save the results: ")
with open(filename, "w") as file:
    #player information
    file.write("playerinformation:\n")

    #Saves each player information using python automatically concatenation
    # of adjacent strings:
    for each_player in players:
        file.write(
            f"Name: {each_player['name']}\n"
            f"* E-mail: {each_player['email']}\n"
            f"* Country: {each_player['country']}\n"
            f"* Wins: {each_player['wins']}\n\n"
            )
            

    # Round history
    file.write("\nGame rounds:\n")
    for r in range(rounds):
        # Start with empty text for this round
        rolls_str = ""

        # Go through each player and build the string step by step
        for i, each_player in enumerate(players):
            rolls_str += f"{each_player['name']} rolled {each_player['rolls'][r]}"
            # Add a comma and space unless it's the last player:
            if i < len(players) - 1:
                rolls_str += ", "

        # Now write the full round info to the file:
        file.write(f"Round {r+1}:\n {rolls_str}\n")

print("\nGame over! Results saved successfully.")
