def rotate(wp,deg):
    if deg < 0: # deg -> +/- 90,180,270
        deg = 360 + deg    
    while deg > 0:
        wp = (wp[1],-wp[0])
        deg -= 90
    return wp

if __name__ == "__main__":
    with open("day12.input") as f:
        instructions = [ (line[0], int(line[1:])) for line in f.readlines() ]
    
    curr = (0,0)
    direction = 1 # 0N 1E 2S 3W
    for op, qt in instructions:
        curr = (curr[0] + qt * ((op=="E") - (op=="W") + ((op=="F") * ((direction==1) - (direction==3)))),
                curr[1] + qt * ((op=="N") - (op=="S") + ((op=="F") * ((direction==0) - (direction==2)))))
        direction = (direction + qt//90 * ((op=="R")-(op=="L"))) % 4

    print(abs(curr[0]) + abs(curr[1]))

    curr = (0,0)
    waypoint = (10,1)
    for op, qt in instructions:
        waypoint = (waypoint[0] + qt * ((op=="E") - (op=="W")),
                    waypoint[1] + qt * ((op=="N") - (op=="S")))

        curr = (curr[0] + (op=="F") * (waypoint[0] * qt),
                curr[1] + (op=="F") * (waypoint[1] * qt))

        waypoint = rotate(waypoint, ((op=="R")-(op=="L")) * qt)

    print(abs(curr[0]) + abs(curr[1]))