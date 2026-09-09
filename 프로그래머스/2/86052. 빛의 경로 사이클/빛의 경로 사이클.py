def solution(grid):
    
    def next(r, c, di_idx):
        
        di = directions[di_idx]
        
        nr = (r + di[0]) % len(grid)
        nc = (c + di[1]) % len(grid[0])
        
        letter = grid[nr][nc]
        if letter == 'S':
            next_di_idx = di_idx
        elif letter == 'L':
            next_di_idx = (di_idx + 1) % 4
        elif letter == 'R':
            next_di_idx = (4 +(di_idx -1)) % 4
        return tuple([nr, nc, next_di_idx])
    
    directions = ((0, 1), (-1, 0), (0, -1), (1, 0))  # 동/북/서/남

    visited = [ [[False] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid)) ]
       
    answer = []
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for idx in range(4):
                
                if visited[r][c][idx]: continue
                
                history = []
                way = (r, c, idx)
                
                
                while visited[way[0]][way[1]][way[2]] == False:
                    visited[way[0]][way[1]][way[2]] = True
                    history.append(way)
                    
                    way = next(way[0], way[1], way[2])
                    
                if way in history:
                    idx = history.index(way)
                    length = len(history) - idx
                    answer.append(length)
                else: pass

    return sorted(answer)