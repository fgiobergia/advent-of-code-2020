# day 20: I'm failing to remember what clean code looked like

import numpy as np # using some shortcuts here
from functools import reduce

def get_sides(tile):
    """
    .2222.
    0    1
    0    1
    0    1
    .3333.
    """
    return [tile[:,0], tile[:,-1],tile[0,:],tile[-1,:]]

class Tile:
    def __init__(self, tile_num, tile):
        self.tile_num = tile_num
        self.tile = np.array(tile)
        self.sides = get_sides(self.tile)
    
    def do_stuff(self, horiz, vert, k, undo=False):
        if undo and k:
            self.tile = np.rot90(self.tile, k)
        if horiz:
            self.tile = self.tile[::-1,:]
        if vert:
            self.tile = self.tile[:,::-1]
        if not undo and k:
            self.tile = np.rot90(self.tile, -k)
        self.sides = get_sides(self.tile)
   
class BunchaTiles:
    def __init__(self, tile):
        self.tiles = [tile]
        self.pos = [(0,0)]
    
    def is_valid(self,i,j):
        if (i,j) in self.pos:
            return []
        return [ k for k in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] if k in self.pos ]
    
    def rescale(self):
        min_y, _, min_x, _ = self.bounds()
        self.pos = [(a-min_y, b-min_x) for a,b in self.pos ]
    
    def bounds(self):
        min_y = min(self.pos, key=lambda x: x[0])[0]
        max_y = max(self.pos, key=lambda x: x[0])[0]
        min_x = min(self.pos, key=lambda x: x[1])[1]
        max_x = max(self.pos, key=lambda x: x[1])[1]
        return min_y, max_y, min_x, max_x
    
    def add_tile(self, other):
        # try and stick the tile anywhere
        min_y, max_y, min_x, max_x = self.bounds()
        for i in range(min_y-1,max_y+2):
            for j in range(min_x-1,max_x+2):
                valid_neighs = self.is_valid(i,j)
                if not valid_neighs: # no useful places
                    continue
                # try all possible rotations!!
                for hor,ver,k in [(0,0,0),(0,1,0),(1,0,0),(0,0,1),(0,0,2),(0,0,3),(0,1,1),(0,1,3)]:
                        other.do_stuff(hor,ver,k)
                        invalid = False
                        # (i,j) is a valid
                        for ni,nj in valid_neighs:
                            ntile = self.tiles[self.pos.index((ni,nj))]
                            ops = [(ni==i+1,2,3), (ni==i-1,3,2),(nj==j-1,1,0),(nj==j+1,0,1)]
                            for match,ndx1,ndx2 in ops:
                                if match and (ntile.sides[ndx1] != other.sides[ndx2]).any():
                                    invalid = True
                                    break
                            if invalid:
                                break
                        if not invalid: # all neighbors match!
                            self.pos.append((i,j))
                            self.tiles.append(other)
                            return True
                        else:
                            other.do_stuff(hor,ver,k,undo=True) # restore initial conditions
        return False

if __name__ == "__main__":
    with open("day20.input") as f:
        tiles = []
        tile = []
        for line in f.readlines():
            line = line.strip()
            if line.startswith("Tile"):
                curr_tile = int(line[5:-1])
            elif not line:
                tiles.append(Tile(curr_tile, tile))
                tile = []
            else:
                tile.append(list(line))
    
    buncha = BunchaTiles(tiles.pop(0))

    while tiles:
        for t in tiles:
            if buncha.add_tile(t):
                tiles.remove(t)
                break
    
    min_y, max_y, min_x, max_x = buncha.bounds()
    print(reduce(lambda a,b: a*b, [ buncha.tiles[buncha.pos.index(k)].tile_num for k in [(min_y, min_x), (min_y,max_x), (max_y,min_x), (max_y,max_x)]]))

    buncha.rescale()
    g = [ [ None for _ in range(max_x-min_x+1) ] for _ in range(max_y-min_y+1) ]
    for p,(i,j) in enumerate(buncha.pos):
        g[i][j] = buncha.tiles[p].tile[1:-1,1:-1]
    grid = np.block(g)

    monster = np.array(
        [
            list("                  # "),
            list("#    ##    ##    ###"),
            list(" #  #  #  #  #  #   "),
        ]
    )
    monster_tile = Tile("🐉", monster)

    # try a bunch of rotations and flips (borrowed from previous exercise)
    for hor,ver,k in [(0,0,0),(0,1,0),(1,0,0),(0,0,1),(0,0,2),(0,0,3),(0,1,1),(0,1,3)]:
        monster_tile.do_stuff(hor,ver,k)
        bool_monster = monster_tile.tile=="#"

        for i in range(len(grid)-bool_monster.shape[0]):
            for j in range(len(grid[i])-bool_monster.shape[1]):
                if (((grid[i:i+bool_monster.shape[0],j:j+bool_monster.shape[1]]==monster_tile.tile) & bool_monster) == bool_monster).all():
                    grid[i:i+bool_monster.shape[0],j:j+bool_monster.shape[1]][bool_monster] = '0'
        
        monster_tile.do_stuff(hor,ver,k,undo=True)
    
    print((grid=="#").sum())