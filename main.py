n = 12
field = [[0] * n for i in range(n)]


def print_field():
    for i in range(0, n):
        print(field[i])


turn = 0
while True:
    puty, putx = (int(x) for x in input().split())

    if field[puty][putx] != 0:
        print("already filled")
        continue
    if (0 > puty > n) or (0 > putx > n):
        print("out of range")
        continue
    if turn == 0:
        field[puty][putx] = 1
    else:
        field[puty][putx] = 2
    print_field()

    tmp_x = 0
    tmp_o = 0
    for i in range(0, n):
        if field[puty][i] == 1:
            tmp_o += 1
            tmp_x = 0
        elif field[puty][i] == 2:
            tmp_x += 1
            tmp_o = 0
        else:
            tmp_x = 0
            tmp_o = 0
        if tmp_o == 5:
            print("player 1 win")
            exit()
        if tmp_x == 5:
            print("player 2 win")
            exit()

    tmp_x = 0
    tmp_o = 0
    for i in range(0, n):
        if field[i][putx] == 1:
            tmp_o += 1
            tmp_x = 0
        elif field[i][putx] == 2:
            tmp_x += 1
            tmp_o = 0
        else:
            tmp_x = 0
            tmp_o = 0
        if tmp_o == 5:
            print("player 1 win")
            exit()
        if tmp_x == 5:
            print("player 2 win")
            exit()

    tmp_x = 0
    tmp_o = 0
    x = putx
    y = puty
    if x > y:
        x = x - y
        y = 0
    else:
        y = y - x
        x = 0
    while (0 <= x < n) and (0 <= y < n):
        if field[y][x] == 1:
            tmp_o += 1
            tmp_x = 0
        elif field[y][x] == 2:
            tmp_x += 1
            tmp_o = 0
        else:
            tmp_x = 0
            tmp_o = 0
        if tmp_o == 5:
            print("player 1 win")
            exit()
        if tmp_x == 5:
            print("player 2 win")
            exit()
        x += 1
        y += 1

    tmp_x = 0
    tmp_o = 0
    x = putx
    y = puty
    start = putx + puty
    if x + y < n:
        while 0 <= x < n and 0 <= start < n:
            if field[start][x] == 1:
                tmp_o += 1
                tmp_x = 0
            elif field[start][x] == 2:
                tmp_x += 1
                tmp_o = 0
            else:
                tmp_x = 0
                tmp_o = 0
            if tmp_o == 5:
                print("player 1 win")
                exit()
            if tmp_x == 5:
                print("player 2 win")
                exit()
            x += 1
            start -= 1
    else:
        start -= 11
        y = n - 1
        while (0 <= y < n) and (0 <= start < n):
            if field[y][start] == 1:
                tmp_o += 1
                tmp_x = 0
            elif field[y][start] == 2:
                tmp_x += 1
                tmp_o = 0
            else:
                tmp_x = 0
                tmp_o = 0
            if tmp_o == 5:
                print("player 1 win")
                exit()
            if tmp_x == 5:
                print("player 2 win")
                exit()
            y -= 1
            start += 1

    turn ^= 1

