import sys
from collections import deque

if __name__ =='__main__' :

    n, m = map(int, sys.stdin.readline().strip().split())

    positions = list(map(int,sys.stdin.readline().strip().split()))

    nums = deque([ i for i in range(1,n+1)])
    count = 0

    for i in positions :
        while True :
            if nums[0] == i :
                nums.popleft()
                break
            else :
                count = count + 1
                if nums.index(i) <= len(nums) // 2 :
                    nums.append(nums.popleft())
                else :
                    nums.appendleft(nums.pop())

    print(count)