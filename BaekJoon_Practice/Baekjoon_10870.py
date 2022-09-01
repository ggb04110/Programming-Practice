def solution(n) :
    n_list = [0, 1]

    if n < 2 :
        return n_list[n]

    for i in range(n-1) :
        n_list.append(n_list[-2] + n_list[-1])

    return n_list[-1]


if __name__ == '__main__':
    input_value = solution(int(input()))
    print(input_value)
