
#  01 MATRIX (LeetCode 542)
from collections import deque

def updateMatrix(mat) :
    rows, cols = len(mat), len(mat[0])
    queue = deque()

    # Step 1: initialize distances
    dist = [[float('inf')] * cols for _ in range(rows)]

    # Step 2: Push all 0s into queue
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                dist[r][c] = 0
                queue.append((r, c))

    # Step 3: BFS
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions :
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

    return dist






    # 6. Walls and Gates (Leetcode 286)
from collections import deque

def wallsAndGates(rooms) :
    if not rooms:
        return

    rows, cols = len(rooms), len(rooms[0])
    queue = deque()

    # Step 1: Add all gates to queue
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0: #Gate
                queue.append((r,c))

    # Step 2: BFS
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                # Only update empty rooms
                if rooms[nr] [nc] == 2147483647:
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc)) 
                                                        