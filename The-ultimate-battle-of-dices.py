import random
import copy
import pandas as pd

# ===== Dice Game =====
def rollD6():
    return random.randint(1, 6)

print("🎲 Welcome to Cooler Battle of Dices! 🎲")

winning_score = 3

player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []
}

# List to store each player's information
players = []

# Ask user for number of players
while True:
    try:
        number_of_players = int(input("How many players are playing? "))
        if number_of_players > 0:
            break
        print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

for i in range(number_of_players):
    player = copy.deepcopy(player_info)
    player["name"] = input(f"Enter player name {i + 1}: ")
    player["email"] = input(f"Enter player email {i + 1}: ")
    player["country"] = input(f"Enter the country of player {i + 1}: ")
    players.append(player)

gameover = False
rounds_played = 0

while not gameover:
    rounds_played += 1
    print(f"\n--- Round {rounds_played} ---")
    input("Press Enter to roll the dice...")

    current_rolls = []

    for each_player in players:
        roll = rollD6()
        current_rolls.append(roll)
        each_player['rolls'].append(roll)
        print(f"🎲 {each_player['name']} rolled: {roll}")

    max_roll = max(current_rolls)
    round_winners = []
    for each_player in players:
        if each_player["rolls"][-1] == max_roll:
            each_player["wins"] += 1
            round_winners.append(each_player['name'])

    print(f"🏆 Round winners: {', '.join(round_winners)}!")

    for each_player in players:
        if each_player["wins"] >= winning_score:
            print(f"\n🎉 {each_player['name']} wins the game with {each_player['wins']} wins! Great battle!")
            gameover = True
            break

    if not gameover:
        print("\nContinuing to next round...")
        print("────────────────────────────")

# Save logs to text file with any name the user wants
filename = input("\nEnter a filename to save the log history: ") + ".txt"
with open(filename, 'w') as file:
    file.write("Player Information:\n")
    for each_player in players:
        file.write(
            f"Name: {each_player['name']}\n"
            f"Email: {each_player['email']}\n"
            f"Country: {each_player['country']}\n"
            f"Wins: {each_player['wins']}\n\n"
        )

    file.write("\nGame Rounds:\n")
    for r in range(rounds_played):
        rolls_str = ", ".join(
            f"{each_player['name']} rolled {each_player['rolls'][r]}"
            for each_player in players
        )
        file.write(f"Round {r + 1}: {rolls_str}\n")

print("\n✅ Game over! Results saved successfully.")

# ===== LogAnalyser =====
class LogAnalyser:
    def __init__(self):
        self.data = []
        self.player_names = []
        self.df = pd.DataFrame()
        
    def load_file(self, filename):
        self.data = []
        self.player_names = []
        
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("❌ File not found!")
            return

        for line in lines:
            if ":" not in line:
                continue
            round_part, rolls_part = line.strip().split(":", 1)
            rolls_dict = {}
            for part in rolls_part.split(","):
                part = part.strip()
                if " rolled " in part:
                    name, _, roll = part.partition(" rolled ")
                    rolls_dict[name] = int(roll)
                    if name not in self.player_names:
                        self.player_names.append(name)
            if rolls_dict:
                self.data.append(rolls_dict)

        self.df = pd.DataFrame(self.data, columns=self.player_names)
        self.df.index += 1  
        self.df.index.name = "Round"

# Load the log file using LogAnalyser
mylog = LogAnalyser()
mylog.load_file(filename)
print("\n📊 Game Roll Analysis:\n")
print(mylog.df)
