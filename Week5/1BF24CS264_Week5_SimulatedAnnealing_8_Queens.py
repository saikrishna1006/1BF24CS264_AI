
import random
import math

# Calculate number of attacking queen pairs
def heuristic(board):
    conflicts = 0

    for i in range(8):
        for j in range(i + 1, 8):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# Simulated Annealing algorithm
def simulated_annealing():
    # Initial random board
    board = [random.randint(0, 7) for _ in range(8)]

    T = 1000
    cooling_rate = 0.95
    Tmin = 0.001

    while T > Tmin:

        current_h = heuristic(board)

        # Check goal state
        if current_h == 0:
            return board

        # Generate neighboring state
        new_board = board[:]
        col = random.randint(0, 7)
        row = random.randint(0, 7)

        new_board[col] = row

        new_h = heuristic(new_board)

        # Calculate energy difference
        delta = current_h - new_h

        # Accept better or probabilistically accept worse state
        if delta > 0:
            board = new_board
        else:
            probability = math.exp(delta / T)

            if random.random() < probability:
                board = new_board

        # Reduce temperature
        T = T * cooling_rate

    if heuristic(board) == 0:
        return board
    else:
        return None


# Display chessboard
def display_board(board):
    for row in range(8):
        for col in range(8):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Main program
solution = simulated_annealing()

if solution:
    print("Solution Found:")
    display_board(solution)
    print("Heuristic Value:", heuristic(solution))
else:
    print("Solution Not Found")
