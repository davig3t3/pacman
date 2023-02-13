import random

square_matrix_size = int(input("Enter the size of the square matrix: "))
matrix = []

# Creating a matrix of size square_matrix_size x square_matrix_size.
for i in range(square_matrix_size):
    matrix.append([0] * square_matrix_size)

# Filling the matrix with ".", "O", and "A".
for i in range(square_matrix_size):
    for j in range(square_matrix_size):
        if i == 0 and j == 0:
            matrix[i][j] = "."
        else:
            matrix[i][j] = random.choice([".", "O", "A"])

points = 0
continue_playing = True
found_A = False
# A loop that will run until the user decides to stop playing.
while continue_playing:
    # Checking if the user has found an A or an O. If the user finds an A, the game will end. If the
    # user finds an O, the user will get a point.
    for i in range(square_matrix_size):
        if i % 2 == 0:
            # This is the code that will run if the row number is even. It will check if the user has
            # found an O or an A. If the user finds an O, the user will get a point. If the user finds
            # an A, the game will end.
            for j in range(square_matrix_size):
                if matrix[i][j] == "O":
                    points += 1
                if matrix[i][j] == "A":
                    found_A = True
                    continue_playing = False
                    break
            if not continue_playing:
                break
        else:
            # Checking if the user has found an O or an A. If the user finds an O, the user will get a
            # point. If the user finds an A, the game will end.
            for j in range(square_matrix_size - 1, -1, -1):
                if matrix[i][j] == "O":
                    points += 1
                if matrix[i][j] == "A":
                    found_A = True
                    continue_playing = False
                    break
            if not continue_playing:
                break
    # Printing the matrix and the points.
    for row in matrix:
        print(row)
    print("Points:", points)
    # This is the code that will run if the user finds an A. It will ask the user if he/she wants to
    # continue playing. If the user says yes, the game will restart. If the user says no, the game
    # will end.
    if found_A:
        option = input("An A was found. Do you want to continue playing? (y/n)").lower()
        # This code is restarting the game.
        if option == "y":
            points = 0
            matrix = []
            for i in range(square_matrix_size):
                matrix.append([0] * square_matrix_size)
            for i in range(square_matrix_size):
                for j in range(square_matrix_size):
                    if i == 0 and j == 0:
                        matrix[i][j] = "."
                    else:
                        matrix[i][j] = random.choice([".", "O", "A"])
            continue_playing = True
            found_A = False
        else:
            continue_playing = False

print("Thank you for playing!")
