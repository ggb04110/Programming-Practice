import sys

if __name__ =='__main__' :

    n = int(sys.stdin.readline().strip())

    rope_list =[]
    for i in range(n) :
        rope = int(sys.stdin.readline().strip())
        rope_list.append(rope)

    rope_list = sorted(rope_list,reverse=True)

    result = []

    for i in range(1,n+1) :
        w = i * rope_list[i-1]
        result.append(w)

    print(max(result))

