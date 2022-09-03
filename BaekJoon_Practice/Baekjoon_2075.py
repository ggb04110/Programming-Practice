import sys
import heapq

if __name__ =='__main__' :
    n = int(sys.stdin.readline().strip())
    heap = []

    for i in range(n) :
        m =  list(map(int, sys.stdin.readline().strip().split()))

        for j in range(n) :
            heapq.heappush(heap,m[j])
            # 최소힙을 만든 후 , 불필요한 메모리 제거
            if len(heap) > n :
                heapq.heappop(heap)

    print(heap[0])