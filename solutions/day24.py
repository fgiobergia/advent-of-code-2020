def count_neighbors(tile, black, mapper):
    return sum(1 for a,b in mapper.values() if (tile[0]+a,tile[1]+b) in black)

if __name__ == "__main__":
    with open("day24.input") as f:
        directions = [ line.strip() for line in f.readlines() ]
    
    mapper = {
        "w": (-1,0),"nw":(0,1),"ne":(1,1),"e":(1,0),"se":(0,-1),"sw":(-1,-1)
    }
    black = set()

    for direction in directions:
        coords = [0,0]
        i = 0
        while i < len(direction):
            d = direction[i]
            if d in "ns":
                i += 1
                d += direction[i]
            coords[0] += mapper[d][0]
            coords[1] += mapper[d][1]
            i += 1
        coords_tuple = tuple(coords)
        if coords_tuple in black:
            black.remove(coords_tuple)
        else:
            black.add(coords_tuple)
    print(len(black))

    for i in range(100):
        new_black = set()
        for tile in black:
            neigh = count_neighbors(tile, black, mapper)
            if neigh != 0 and neigh <= 2:
                new_black.add(tile)
            for a,b in mapper.values():
                n_tile = (tile[0]+a, tile[1]+b)
                if n_tile not in black: # only consider white tiles, black tiles are already handled
                    neigh = count_neighbors(n_tile, black, mapper)
                    if neigh == 2:
                        new_black.add(n_tile)
        black = new_black
    print(len(black))