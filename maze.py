import random

# Define the maze
maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

# Define player's starting position
player_position = [1, 1]

# Define the exit position
exit_position = [5, 8]

# Function to print the maze
def print_maze():
    for row in maze:
        print("".join(row))

# Function to check if the player has won
def check_win():
    return player_position == exit_position

# Main game loop
while True:
    # Print the maze
    print_maze()

    # Check if player has won
    if check_win():
        print("Congratulations! You've won the game!")
        break

    # Get user input
    direction = input("Enter your move (w/a/s/d): ")

    # Update player's position based on input
    if direction == "w" and maze[player_position[0]-1][player_position[1]] != "#":
        player_position[0] -= 1
    elif direction == "a" and maze[player_position[0]][player_position[1]-1] != "#":
        player_position[1] -= 1
    elif direction == "s" and maze[player_position[0]+1][player_position[1]] != "#":
        player_position[0] += 1
    elif direction == "d" and maze[player_position[0]][player_position[1]+1] != "#":
        player_position[1] += 1

    # Clear the console (for better visibility)
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

print("Thanks for playing!")
