from collections import deque

def s_p_Binary_matrix(grid):
    rows, cols = len(grid), len(grid[0])
    
    # If start or end is blocked
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1
    
    # 8 directions (including diagonals)
    directions = [
        (1,0), (-1,0), (0,1), (0,-1),
        (1,1), (1,-1), (-1,1), (-1,-1)
    ]

    queue = deque([(0, 0, 1)])  # (row, col, distance)
    visited = set([(0, 0)])

    while queue:
        r, c, dist = queue.popleft()

        # Reached destination
        if r == rows-1 and c == cols-1:
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))

    return -1

grid = [
    [0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0]
]
print(s_p_Binary_matrix(grid))
