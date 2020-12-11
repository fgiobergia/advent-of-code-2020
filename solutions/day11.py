def in_bounds(grid, a, b):
    return 0<=a<len(grid) and 0<=b<len(grid[a])

def neighbors(grid, y, x, search):
    a = b = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i or j:
                off_i = i
                off_j = j
                while in_bounds(grid, y+off_i, x+off_j) and grid[y+off_i][x+off_j]=="." and search:
                    off_i += i
                    off_j += j
                
                a += not in_bounds(grid,y+off_i,x+off_j) or grid[y+off_i][x+off_j] in "L."
                b += in_bounds(grid,y+off_i,x+off_j) and grid[y+off_i][x+off_j] == "#"
    return a,b

def choose(neigh, curr, thresh):
    if curr == ".":
        return "."
    if neigh[0] == 8:
        return "#"
    if neigh[1] >= thresh and curr == "#":
        return "L"
    return curr

def simulate(grid, search, neigh):
    while True:
        # not particularly efficient, but eh
        new_grid = [ [ choose(neighbors(grid,y,x,search), grid[y][x], neigh) for x in range(len(grid[y])) ] for y in range(len(grid)) ]
        if new_grid == grid:
            break
        grid = new_grid
    return sum(x.count("#") for x in new_grid )

if __name__ == "__main__":
    with open("day11.input") as f:
        grid = [ list(line.strip()) for line in f.readlines() ]

    print(simulate(grid,False,4))
    print(simulate(grid,True,5))