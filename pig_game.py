import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Entr the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again")

max_score = 25
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_index in range(players):
        print("\nPlayer", player_index + 1, "turn has just started!\n")
        print("Your total score is:", player_scores[player_index],"\n")
        current_score = 0
        while True:
            
            should_roll = input("\nwould you like to roll (y)? ")
            if should_roll.lower() != 'y':
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 1
                break
            else:
                current_score += value
                print("You rolled a:", value)
        
            print("Your score is:", current_score)
        
        player_scores[player_index] += current_score

        print("Your total score is:", player_scores[player_index])

print("Game has ended!")
print("Player", player_scores.index(max(player_scores))+1, "is the winner!")

for i in range(len(player_scores)):
    print("\n Player:", i+1, "Points:", player_scores[i])
