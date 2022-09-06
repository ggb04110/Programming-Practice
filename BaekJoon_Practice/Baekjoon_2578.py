import sys

def solution(board,n) :

    for i in range(5) :
        for j in range(5) :
            if board[i][j] == n :
                board[i][j] = 0
                return board

    return

def check_board(board) :

    count = 0
    check_left_diag_bingo = True
    check_right_diag_bingo = True

    for i in range(5) :
        check_row = board[i][0]
        check_column = board[0][i]
        chk_row_bingo = True
        chk_column_bingo = True

        for j in range(5) :
            if check_row != board[i][j] :
                chk_row_bingo = False

            if check_column != board[j][i] :
                chk_column_bingo = False

        if chk_row_bingo == True :
            count = count + 1

        if chk_column_bingo == True :
            count = count + 1

        if board[0][0] != board[i][i] :
            check_left_diag_bingo = False

        if board[0][4] != board[i][4-i] :
            check_right_diag_bingo = False

    if check_left_diag_bingo == True :
        count = count + 1

    if check_right_diag_bingo == True :
        count = count + 1

    return count


if __name__ =='__main__' :

    board = []

    for i in range(5) :
        temp = list(map(int,sys.stdin.readline().strip().split()))
        board.append(temp)

    answer = 0
    for i in range(5) :
        temp = list(map(int, sys.stdin.readline().strip().split()))
        for d in temp :
            answer = answer + 1
            board = solution(board,d)
            chk_count = check_board(board)
            if chk_count >= 3 :
                print(answer)
                exit(0)


