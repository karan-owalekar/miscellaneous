import random

switch_door = True
total_iterations = 1000

winning_count = 0
for _ in range(total_iterations):
    # Randomly select a winning door
    winning_door = random.randint(1, 3)
    # Player's choice
    player_choice = random.randint(1, 3)

    # Open one of the loosing door
    doors = [1, 2, 3]
    doors.remove(player_choice)  # Remove player's choice first
    if player_choice == winning_door: 
        # ALl of the other doors are loosing doors so open one of them randomly
        loosing_door = random.choice(doors)
    else:
        # One of the loosing doors is the winning door so open the other loosing door
        doors.remove(winning_door)
        loosing_door = doors[0]

    available_doors = [1, 2, 3]
    available_doors.remove(loosing_door)

    if switch_door:
        available_doors.remove(player_choice)
        player_choice = available_doors[0]

    if player_choice == winning_door:
        # print("[INFO] Player wins")
        winning_count += 1

print(f"[INFO] Winning probability {"with" if switch_door else "without"} switching doors: {(winning_count / total_iterations)*100} %")