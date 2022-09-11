import sys

def GCD(a,b) :

    while b > 0 :
        a,b = b , a % b


    return a

if __name__ == '__main__' :
    n = int(sys.stdin.readline().strip())

    n_list = list(map(int,sys.stdin.readline().strip().split()))

    for i in range(1,len(n_list)) :
        gcd = GCD(n_list[0],n_list[i])
        print('%d/%d' %(n_list[0]//gcd, n_list[i]//gcd))