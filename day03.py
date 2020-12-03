from functools import reduce
if __name__ == "__main__":
    with open("day03.input") as f:
        grid = [ l.strip() for l in f ]

    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    trees = [   sum(
                    grid[i][((i//down)*right)%len(grid[0])] == "#"
                    for i in range(0,len(grid), down)
                )
                for right, down in slopes
            ]
    
    print(trees[1])
    print(reduce(lambda a,b: a*b, trees, 1))