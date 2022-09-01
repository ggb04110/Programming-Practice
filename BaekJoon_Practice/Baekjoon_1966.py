import sys
from collections import deque

def solution(y,print_list) :

    count = 0
    while print_list :
        if print_list[0][1] == max(list(map(lambda x: x[1], print_list))) :
            count = count + 1
            a, b = print_list.popleft()
            if y == a :
                return count
        else :
            print_list.append(print_list.popleft())

    return

if __name__ == '__main__':

    n = int(input())
    for i in range(n) :
        x, y = map(int, sys.stdin.readline().strip().split())
        input_list = list(map(int,sys.stdin.readline().split()))
        print_list = deque([])
        for i in range(x) :
            print_list.append((i,input_list[i]))
        print(solution(y, print_list))
