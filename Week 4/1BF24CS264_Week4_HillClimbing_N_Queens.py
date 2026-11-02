
import random

def calculate_heuristic(board):
    """
    Calculate the number of pairs of queens
    attacking each other.
    """
    n = len(board)
    conflicts = 0

    for i in range(n):
        for j in range(i + 1, n):
            # Same row or diagonal conflict
            if board[i] == board[j] or \
               abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def hill_climbing(n):
    # Randomly place one queen in each column
    board = [random.randint(0, n - 1) for _ in range(n)]

    while True:
        current_h = calculate_heuristic(board)

        # Goal state: no conflicts
        if current_h == 0:
            return board

        best_board = board[:]
        best_h = current_h

        # Generate neighboring states
        for col in range(n):
            for row in range(n):
                if row != board[col]:
                    neighbor = board[:]
                    neighbor[col] = row

                    h = calculate_heuristic(neighbor)

                    if h < best_h:
                        best_h = h
                        best_board = neighbor

        # Stop if no better neighbor exists
        if best_h >= current_h:
            return None

        board = best_board


def print_board(board):
    n = len(board)

    for row in range(n):
        for col in range(n):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Main program
n = int(input("Enter the value of N: "))

solution = hill_climbing(n)

if solution:
    print("\nSolution found:")
    print_board(solution)
    print("Heuristic value:", calculate_heuristic(solution))
else:
    print("\nLocal optimum reached! No solution found.")
