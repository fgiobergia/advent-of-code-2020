def func(start, goal):
    history = {}

    curr_turn = 0
    while curr_turn < goal:
        if curr_turn < len(start):
            num = start[curr_turn]
        else:
            num = next_num
        if num not in history:
            utterance = 0
        else:
            utterance = curr_turn - history[num]

        history[num] = curr_turn

        next_num = utterance
        curr_turn += 1
    return num

if __name__ == "__main__":
    start = [6,3,15,13,1,0]
    print(func(start, 2020))
    # execution time: ~ 14s (heh)
    print(func(start, 30000000))