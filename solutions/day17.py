
def count_neighbors(coord, active, c, curr_dim, num_dim):
    if curr_dim == num_dim:
        return tuple(c) in active and coord != c

    res = 0
    for i in range(coord[curr_dim]-1, coord[curr_dim]+2):
        c[curr_dim] = i
        res += count_neighbors(coord, active, c, curr_dim+1, num_dim)
    return res

def get_new_active(new_active, active, ranges, curr_pos, curr_dim, n_dim):
    if curr_dim == n_dim:
        n_neigh = count_neighbors(curr_pos, active, [0]*n_dim, 0, n_dim)
        tpl = tuple(curr_pos)
        if tpl in active:
            if 2 <= n_neigh <= 3:
                new_active.add(tpl)
        else:
            if n_neigh == 3:
                new_active.add(tpl)
        return
    
    for i in range(ranges[curr_dim][0]-1, ranges[curr_dim][1]+2):
        curr_pos[curr_dim] = i
        get_new_active(new_active, active, ranges, curr_pos, curr_dim+1, n_dim)

def run_boot(grid, n_dim):
    active = { (j,i) + (0,)*(n_dim-2)  for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "#" } # list of active cells (x,y,z)
    for i in range(6):
        ranges = [
            (min(active, key=lambda x: x[i])[i], max(active, key=lambda x: x[i])[i])
            for i in range(n_dim)
        ]
        new_active = set()

        get_new_active(new_active, active, ranges, [0]*n_dim, 0, n_dim)
        active = new_active
    return len(new_active)

if __name__ == "__main__":
    with open("day17.input") as f:
        grid = [ line.strip() for line in f.readlines() ]
    
    print(run_boot(grid, 3))
    print(run_boot(grid, 4))