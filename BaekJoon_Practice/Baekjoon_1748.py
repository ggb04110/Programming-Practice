import sys

if __name__ == '__main__' :

    n = int(sys.stdin.readline().strip())

    pre_sum = 0
    for i in range(1,len(str(n))+1) :
        if i < len(str(n)) :
            pre_sum = pre_sum + ((10**i)-1-(10**(i-1))+1)*i
        else :
            pre_sum = pre_sum + ((n-10**(i-1))+1)*i

    print(pre_sum)

