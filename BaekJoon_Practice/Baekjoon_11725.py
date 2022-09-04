import sys
from collections import defaultdict
from collections import deque

def dfs(n,tree_graph) :
    visited = [False for _ in range(n+1)]
    queue = deque([])
    queue.append(1)
    visited[1] = True
    result = [1 for _ in range(n+1) ]
    while queue :
        node = queue.popleft()
        for i in tree_graph[node] :
            if visited[i] == True :
                continue
            else :
                visited[i] = True
                queue.append(i)
                result[i] = node

    return result[2:]

if __name__ =='__main__' :
    n = int(sys.stdin.readline().strip())

    tree_graph = defaultdict(list)
    for i in range(n-1) :
        x, y = map(int, sys.stdin.readline().strip().split())
        tree_graph[x].append(y)
        tree_graph[y].append(x)

    for i in dfs(n,tree_graph) :
        print(i)
