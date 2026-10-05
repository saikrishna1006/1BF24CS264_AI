def heuristic(state, goal):
    distance = 0

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                continue

            for x in range(3):
                for y in range(3):
                    if goal[x][y] == state[i][j]:
                        distance += abs(i - x) + abs(j - y)

    return distance


def get_neighbors(state):
    neighbors = []

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                row, col = i, j

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [list(r) for r in state]

            new_state[row][col], new_state[new_row][new_col] = \
                new_state[new_row][new_col], new_state[row][col]

            neighbors.append(tuple(tuple(r) for r in new_state))

    return neighbors


def a_star(start, goal):
    OPEN = []
    CLOSED = set()

    g = {}
    f = {}
    parent = {}

    start = tuple(tuple(row) for row in start)
    goal = tuple(tuple(row) for row in goal)

    OPEN.append(start)

    g[start] = 0
    f[start] = heuristic(start, goal)
    parent[start] = None

    while OPEN:
        n = min(OPEN, key=lambda state: f[state])

        if n == goal:
            path = []

            while n is not None:
                path.append(n)
                n = parent[n]

            path.reverse()
            return path

        OPEN.remove(n)
        CLOSED.add(n)

        for m in get_neighbors(n):
            if m in CLOSED:
                continue

            g_new = g[n] + 1

            if m not in OPEN or g_new < g[m]:
                parent[m] = n
                g[m] = g_new
                f[m] = g[m] + heuristic(m, goal)

                if m not in OPEN:
                    OPEN.append(m)

    return None


start = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

goal = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

path = a_star(start, goal)

if path:
    print("Solution found!")
    print("Number of moves:", len(path) - 1)

    for step, state in enumerate(path):
        print("\nStep", step)

        for row in state:
            print(row)
else:
    print("No solution exists")
