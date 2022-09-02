import sys

if __name__ == '__main__':

    x, y = map(int, sys.stdin.readline().strip().split())

    s_list = []
    for i in range(x) :
        s = sys.stdin.readline().strip()
        s_list.append(s)

    result = []
    count = 0
    for i in range(y) :
        alpha_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for j in range(x) :
            alpha_dict[s_list[j][i]] = alpha_dict.get(s_list[j][i],0) + 1

        for n, m in alpha_dict.items() :
            if m == max(alpha_dict.values()) :
                count = count + x-m
                result.append(n)
                break


    print(''.join(result))
    print(count)