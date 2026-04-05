from collections import deque

def cutTree(f):
    rows, cols = len(f), len(f[0])
    
    trees = []
    for r in range(rows):
        for c in range(cols):
            if f[r][c] > 1:
                trees.append((f[r][c], r, c))
                
    trees.sort()
    
    
    def bfs(sr, sc, tr, tc):
        if sr == tr and sc == tc:
            return 0
        
        visited = set([(sr, sc)])
        queue = deque([(sr, sc, 0)])
        
        while queue:
            r, c, steps = queue.popleft()
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) not in visited and f[nr][nc] != 0:
                        if nr == tr and nc == tc:
                            return steps + 1

                        visited.add((nr, nc))
                        queue.append((nr, nc, steps + 1))

        return -1

    # Step 3: walk through trees
    total_steps = 0
    sr, sc = 0, 0

    for _, tr, tc in trees:
        steps = bfs(sr, sc, tr, tc)
        if steps == -1:
            return -1

        total_steps += steps
        sr, sc = tr, tc  # move to new position

    return total_steps 

forest = [
    [1, 2, 0, 4, 5, 6],
    [0, 0, 7, 0, 0, 8],
    [9,10,11, 0,13,14],
    [0, 0,15, 0, 0,16],
    [17,18,19,20,21,22]
]
print(cutTree(forest))