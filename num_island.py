# idea is to count how many seperate islands exist
# steps:
# 1. loop through grids
# 2. when '1' has been located srart the bfs
# 3. mark all connected '1' as visited
# 4. increase count.


from collections import deque

def num_island(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    for r in range (rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                queue =  deque

                while queue:
                    x, y = queue.popleft()
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == "1":
                        grid[x][y] = "0"
                        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                            queue.append((x+dx, y+dy))
    return count                        