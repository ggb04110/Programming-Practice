import sys

if __name__ == '__main__':

    n = int(input())

    cow_dict = {}
    count = 0
    for i in range(n) :
        x, y = map(int, sys.stdin.readline().strip().split())
        if x in cow_dict.keys() :
            if y == cow_dict[x] :
                continue
            else :
                count = count + 1
                cow_dict[x] = y
        else :
            cow_dict[x] = y

    print(count)