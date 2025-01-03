from collections import deque 

grid = []
with open('data.txt', 'r') as file: 
    for line in file: 
        grid.append(list(line.strip()))
    
rows = len(grid)
cols = len(grid[0])

directions = [[-1,0], [1,0], [0,1], [0,-1]] 
visited = set() 

def bfs(letter, r,c):
    q = deque()

    q.append((r,c))
    visited.add((r,c))
    area = 1 
    total_perimeter = 0
    while q: 
        row, col = q.popleft()
        perimeter = 4

        for dr, dc in directions: 
            r = row + dr
            c = col + dc 

            if r in range(rows) and c in range(cols):
                if grid[r][c] == letter: 
                    perimeter -=1 

            if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] == letter: 
                q.append((r,c))
                visited.add((r,c))
                area += 1 

                
        total_perimeter += perimeter
    return area * total_perimeter

total_cost = 0 
for i in range(rows): 
    for j in range(cols): 
        if (i,j) not in visited: 
            total_cost += bfs(grid[i][j], i ,j)

print(total_cost)