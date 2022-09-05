import sys

if __name__ =='__main__' :

    n = int(sys.stdin.readline().strip())
    count = 0
    for i in range(n) :
        s = sys.stdin.readline().strip()

        temp = set()
        pre_word = ''
        for ch in s :
            if ch == pre_word :
                continue
            else :
                if ch not in temp :
                    temp.add(ch)
                    pre_word = ch
                else :
                    count = count + 1
                    break

    print(n- count)