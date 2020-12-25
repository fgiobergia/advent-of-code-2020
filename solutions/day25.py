def find_loop_size(target, subject=7):
    i = 0
    val = 1
    while val != target:
        val = (val * subject) % 20201227
        i += 1
    return i

def encryption_key(loop_size, subject):
    i = 0
    val = 1
    for i in range(loop_size):
        val = (val * subject) % 20201227
    return val

if __name__ == "__main__":
    with open("day25.input") as f:
        card_pk, door_pk = map(int, [f.readline(), f.readline()])
    
    loop_size_card = find_loop_size(card_pk)
    loop_size_door = find_loop_size(door_pk)
    print(encryption_key(loop_size_card, door_pk), encryption_key(loop_size_door, card_pk))