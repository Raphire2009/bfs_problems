from collections import deque

def shortest_path(grid, k):
    rows, cols = len(grid), len(grid[0])
    
    queue = deque([(0, 0, k, 0)])
    visited = set()
    visited.add((0, 0, k))
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while queue:
        r, c, remaining_k, steps = queue.popleft()
        
        if r == rows -1 and c == cols -1:
            return steps
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                new_k = remaining_k - grid[nr][nc]
                
                if new_k >= 0 and (nr, nc, new_k) not in visited:
                    visited.add((nr, nc, new_k))
                    queue.append((nr, nc, new_k, steps + 1))
                    
                    
    return -1

grid = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0]
]
k = 2
result = shortest_path(grid, k)
print(result)
