import sys
import heapq

if __name__ =='__main__' :
    n = int(sys.stdin.readline().strip())
    stack = []

    for i in range(n) :
        m = int(sys.stdin.readline().strip())

        if m == 0 :
            if len(stack) == 0 :
                print(0)
                continue
            else :
                temp = heapq.heappop(stack)
                print(temp[1])
        else :
            heapq.heappush(stack, (-m,m))