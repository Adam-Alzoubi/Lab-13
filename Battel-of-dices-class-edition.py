from Dices import rollD6 , rollD4

# Superclass 
class Battle_of_dices:
    def __init__(self, winning_score=5):
        self.rounds = 0
        self.gameover = False
        self.winning_score = winning_score


#  Subclass: Player 
class Player(Battle_of_dices):
    def __init__(self, name, email, country):
        super().__init__()   
        self.name = name
        self.email = email
        self.country = country
        self.wins = 0
        self.rolls = []


#  Subclass: Game 
class Game(Battle_of_dices):
    def __init__(self, players, winning_score=5):
        super().__init__(winning_score=winning_score)  
        self.players = players

    def play(self):
        print(f"\n Welcome to the cooler multiplayer battle of dices 🎲🎲")

        # Play until gameover
        while not self.gameover:
            print(f"\n=== Round {self.rounds+1} ===")
            current_rolls = []

            # Each player rolls dice
            for p in self.players:
                roll = rollD4() + rollD6()
                p.rolls.append(roll)
                current_rolls.append(roll)
                print(f"Player {p.name} rolled {roll}")

            # Determine round winners
            max_roll = max(current_rolls)
            winners = []
            for p in self.players:
                if p.rolls[-1] == max_roll:
                    p.wins += 1
                    print(f"Player {p.name} won in round {self.rounds+1}")
                    winners.append(p.name)

            print(f"Winners of this round: {winners}")

            # Check if someone reached winning score
            for p in self.players:
                if p.wins >= self.winning_score:
                    print(f"\n🏆 {p.name} is the newest and coolest Battle of Dices Champion!")
                    self.gameover = True
                    break

            if not self.gameover:
                print("The battle is still going on...🔥...Who will win in the end?")

            self.rounds += 1

    def save_results(self, filename):
        with open(filename, "w") as file:
            file.write("Player Information:\n")
            for p in self.players:
                file.write(
                    f"Name: {p.name}\n"
                    f"* E-mail: {p.email}\n"
                    f"* Country: {p.country}\n"
                    f"* Wins: {p.wins}\n\n"
                )

            # Round history
            file.write("\nGame Rounds:\n")
            for r in range(self.rounds):
                rolls_str = ""
                for i, p in enumerate(self.players):
                    rolls_str += f"{p.name} rolled {p.rolls[r]}"
                    if i < len(self.players) - 1:
                        rolls_str += ", "
                file.write(f"Round {r+1}:\n {rolls_str}\n")

        print("\nGame over! Results saved successfully.")


# === Main Program ===
if __name__ == "__main__":
    # Get number of players
    num_players = int(input("How many players will play? "))
    players = []

    for i in range(num_players):
        name = input(f"What is the name of player {i+1}? ")
        email = input(f"What is the email of player {i+1}? ")
        country = input(f"What is the country of player {i+1}? ")
        players.append(Player(name, email, country))

    # Start game
    game = Game(players, winning_score=5)
    game.play()

    # Save results
    filename = input("\nEnter the filename to save the results: ")
    game.save_results(filename)
