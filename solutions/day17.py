def count_neighbors(coord, active):
    x,y,z = coord

    neighs = sum([ (nx,ny,nz) in active for nx in range(x-1,x+2) for ny in range(y-1,y+2) for nz in range(z-1,z+2) if nx!=x or ny!=y or nz!=z ])
    return neighs

def count_neighbors_4d(coord, active):
    x,y,z,w = coord

    neighs = sum([ (nx,ny,nz,nw) in active for nx in range(x-1,x+2) for ny in range(y-1,y+2) for nz in range(z-1,z+2) for nw in range(w-1,w+2) if nx!=x or ny!=y or nz!=z or nw!=w])
    return neighs

if __name__ == "__main__":
    with open("day17.input") as f:
        grid = [ line.strip() for line in f.readlines() ]
    
    rx = (0, len(grid[0]))
    ry = (0, len(grid))
    rz = (-1,2)

    active = { (j,i,0) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "#" } # list of active cells (x,y,z)
    for i in range(6):
        x_range = (min(active, key=lambda x: x[0])[0], max(active, key=lambda x: x[0])[0])
        y_range = (min(active, key=lambda x: x[1])[1], max(active, key=lambda x: x[1])[1])
        z_range = (min(active, key=lambda x: x[2])[2], max(active, key=lambda x: x[2])[2])
        new_active = set()
        for x in range(x_range[0]-1, x_range[1]+2):
            for y in range(y_range[0]-1, y_range[1]+2):
                for z in range(z_range[0]-1, z_range[1]+2):
                    n_neigh = count_neighbors((x,y,z), active)
                    if (x,y,z) in active:
                        if 2 <= n_neigh <= 3:
                            new_active.add((x,y,z))
                    else:
                        if n_neigh == 3:
                            new_active.add((x,y,z))
        active = new_active
    print(len(active))

    active = { (j,i,0,0) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "#" } # list of active cells (x,y,z)
    for i in range(6):
        x_range = (min(active, key=lambda x: x[0])[0], max(active, key=lambda x: x[0])[0])
        y_range = (min(active, key=lambda x: x[1])[1], max(active, key=lambda x: x[1])[1])
        z_range = (min(active, key=lambda x: x[2])[2], max(active, key=lambda x: x[2])[2])
        w_range = (min(active, key=lambda x: x[3])[3], max(active, key=lambda x: x[3])[3])
        new_active = set()
        for x in range(x_range[0]-1, x_range[1]+2):
            for y in range(y_range[0]-1, y_range[1]+2):
                for z in range(z_range[0]-1, z_range[1]+2):
                    for w in range(w_range[0]-1, w_range[1]+2):
                        n_neigh = count_neighbors_4d((x,y,z,w), active)
                        if (x,y,z,w) in active:
                            if 2 <= n_neigh <= 3:
                                new_active.add((x,y,z,w))
                        else:
                            if n_neigh == 3:
                                new_active.add((x,y,z,w))
        active = new_active
    print(len(active))