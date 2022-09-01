import sys

if __name__ == '__main__':

    n, m = map(int, sys.stdin.readline().strip().split())

    n_dict = {}

    for i in range(n) :
        word = sys.stdin.readline().strip()
        n_dict[word] = n_dict.get(word,0) + 1

    count = 0
    for i in range(m) :
        word = sys.stdin.readline().strip()
        if word in n_dict.keys() :
            count = count + 1

    print(count)