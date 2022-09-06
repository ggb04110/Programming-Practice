import sys

if __name__ =='__main__' :

    n = int(sys.stdin.readline().strip())

    find_num = int(sys.stdin.readline().strip())

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    result = [ [0 for _ in range (n)]  for _ in range(n)]

    result[0][0] = n*n

    count = 0
    x,y = 0,0
    answer_x, answer_y = 1, 1

    while True :

        temp_x = x + dx[count % 4]
        temp_y = y + dy[count % 4]

        if temp_x < 0 or temp_y < 0 or temp_x >= n or temp_y >= n or result[temp_x][temp_y] != 0 :
            count = count + 1
            continue
        else :
            result[temp_x][temp_y] = result[x][y] - 1
            x = temp_x
            y = temp_y

            if result[temp_x][temp_y] == find_num :
                answer_x = x + 1
                answer_y = y + 1

        if x == n//2 and y == n//2 :
             break

    for i in result :
        print(' '.join(list(map(str,i))))
    print(answer_x, answer_y)
