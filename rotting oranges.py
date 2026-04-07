# idea is to spread rot minute by minute
# steps
# 1. put all rotten oranges in a queue first
# 1. spread rotten oranges to fresh ones
# 3. count time (levels = minutes)


from collections import deque

def rotten_oranges(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque
    fresh_oranges = 0

    for r in range(rows):
        for c in range(cols):
            if grid [r][c] == 2:
                queue.append((r,c))
            elif grid[r][c] == 1:
                fresh_oranges += 1
    time = 0

    while queue and fresh_oranges:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc         
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    queue.append((nr, nc))
        time += 1
    return time if fresh_oranges == 0 else -1                
