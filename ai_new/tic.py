board = ['-' for i in range(9)]
def printb():
    for i in range(1,10):
        print(f"{board[i - 1]} ", end = "")
        if i % 3 == 0: 
            print()
def win():
    winc = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for i in winc:
        if board[i[0]] == board[i[1]] == board[i[2]] != '-':
            return True
    return False
def draw():
    if '-' in board:
        return False 
    return True
def tic():
    curr = 'X'
    while True:
        printb()
        move = int(input(f"move for {curr} (1-9): "))
        if board[move - 1] == '-':
            board[move -1] = curr
            if win():
                printb()
                print(f"player {curr} won!!!")
                break
            if draw():
                printb()
                print("draw")
                break
            if curr == 'X':
                curr = 'O'
            else:
                curr = 'X'
        else:
            print("not a valid move")

tic()       

