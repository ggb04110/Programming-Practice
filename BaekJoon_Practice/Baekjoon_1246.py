import sys

if __name__ =='__main__' :

    n, m = map(int, sys.stdin.readline().strip().split())

    p_list = []
    for i in range(m) :
        p = int(sys.stdin.readline().strip())
        p_list.append(p)

    p_list = sorted(p_list)
    max_money = p_list[0] * min(n,m)
    max_price = p_list[0]

    for i in range(m) :
        count = min(n,m-i)
        if p_list[i] *  count > max_money :
            max_price = p_list[i]
            max_money = p_list[i] * count

    print(max_price, max_money)
