import sys

if __name__ =='__main__' :
    n = int(sys.stdin.readline().strip())

    n_list = list(map(int,sys.stdin.readline().strip().split()))

    prefix_sum = 0
    result = 0

    for i in range(len(n_list)-1) :
        prefix_sum = prefix_sum + n_list[i]
        result = result + n_list[i+1] * prefix_sum

    print(result)
