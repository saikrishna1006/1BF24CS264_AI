
N = 4

# Calculate heuristic value
def heuristic(board):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if (board[i] == board[j] or
                abs(board[i] - board[j]) == abs(i - j)):
                conflicts += 1

    return conflicts


# Display chessboard
def display_board(board):
    for row in range(N):
        for col in range(N):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Hill Climbing algorithm
def hill_climbing(board):
    step = 1

    while True:
        current_h = heuristic(board)

        print("\n========== STEP", step, "==========")
        print("Current State:", board)
        print("Heuristic Value:", current_h)
        display_board(board)

        if current_h == 0:
            print("Goal State Reached!")
            return board

        best_board = board[:]
        best_h = current_h

        print("\nNeighboring States:")

        # Generate neighboring states
        for col in range(N):
            for row in range(N):
                if row != board[col]:
                    neighbor = board[:]
                    neighbor[col] = row

                    h = heuristic(neighbor)

                    print(neighbor, "-> Heuristic:", h)

                    if h < best_h:
                        best_h = h
                        best_board = neighbor

        # Check local optimum
        if best_h >= current_h:
            print("\nLocal Optimum Reached!")
            print("No better neighbor found.")
            return None

        print("\nSelected Best State:", best_board)
        print("Selected Heuristic:", best_h)

        board = best_board
        step += 1


# Main program
print("Enter initial state (16 values between 0 and 15):")
board = list(map(int, input().split()))

if len(board) != N or any(x < 0 or x >= N for x in board):
    print("Invalid Input! Enter exactly 16 values between 0 and 15.")

else:
    solution = hill_climbing(board)

    if solution:
        print("\nFINAL SOLUTION:")
        display_board(solution)
        print("Final Heuristic:", heuristic(solution))
    else:
        print("\nSolution Not Found.")
