import sys

if __name__ == '__main__' :
    n = int(sys.stdin.readline().strip())

    s = []
    for i in range(n) :
        cmd = sys.stdin.readline().strip().split()

        if cmd[0] == 'add' :
            if int(cmd[1]) in s :
                continue
            else :
                s.append(int(cmd[1]))

        if cmd[0] == 'remove' :
            if int(cmd[1]) in s :
                s.remove(int(cmd[1]))

        if cmd[0] == 'check' :
            if int(cmd[1]) in s :
                print(1)
            else :
                print(0)

        if cmd[0] == 'toggle' :
            if int(cmd[1]) in s :
                s.remove(int(cmd[1]))
            else :
                s.append(int(cmd[1]))

        if cmd[0] == 'all' :
            s = [i for i in range(1,21)]

        if cmd[0] == 'empty' :
            s = []
