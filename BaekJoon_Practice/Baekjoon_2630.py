import sys

if __name__ =='__main__' :
    n = int(sys.stdin.readline().strip())

    color_paper = []

    for i in range(n) :
        input_value = list(map(int, sys.stdin.readline().strip().split()))
        color_paper.append(input_value)

    blue= 0
    white = 0


    def solution(x, y, n):
        global white, blue

        color = color_paper[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if color != color_paper[i][j]:
                    solution(x, y, n // 2)
                    solution(x, y + n // 2, n // 2)
                    solution(x + n // 2, y, n // 2)
                    solution(x + n // 2, y + n // 2, n // 2)
                    return

        if color == 0:
            white += 1
        else:
            blue += 1

    solution(0,0,n)

    print(white)
    print(blue)