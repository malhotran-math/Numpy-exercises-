# Create a second 3D array of another game and its solution 
new_game_and_solution = np.array([new_sudoku_game,new_sudoku_solution])

# Create a 4D array of both game and solution 3D arrays
games_and_solutions = np.array([game_and_solution,new_game_and_solution])

# Print the shape of your 4D array
print(games_and_solutions.shape)
