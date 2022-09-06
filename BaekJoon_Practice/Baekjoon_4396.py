import sys

if __name__ =='__main__' :
    n = int(sys.stdin.readline().strip())

    mine_board = []
    for i in range(n) :
        mine_board.append(sys.stdin.readline().strip())

    process_board = []
    for i in range(n) :
        process_board.append(sys.stdin.readline().strip())

    merge_board = [ [] for _ in range(n)]
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [1,0,-1,1,-1,1,0,-1]
    check_mine = False

    for i in range(n) :
        for j in range(n) :
            count = 0
            for d in range(8) :
                temp_x, temp_y =  i - dx[d] , j - dy[d]
                if temp_x < 0 or temp_y < 0 or temp_x >= n or temp_y >= n:
                   continue

                if mine_board[temp_x][temp_y] == '*' :
                    count = count + 1

            if process_board[i][j] == 'x' :
                if mine_board[i][j] == '*' :
                    check_mine = True
                    merge_board[i].append('*')
                else :
                    merge_board[i].append(str(count))
            else :
                merge_board[i].append('.')

    if check_mine == True :
        for i in range(n) :
            for j in range(n) :
                if mine_board[i][j] == '*' :
                    merge_board[i][j] = '*'

    for i in merge_board :
        print(''.join(i))