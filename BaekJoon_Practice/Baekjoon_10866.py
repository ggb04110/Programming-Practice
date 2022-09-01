import sys
from collections import deque
def solution(n) :
    stack_list = deque()
    for i in range(n) :
        cmd = sys.stdin.readline().strip().split()
        if cmd[0] == 'push_front' :
            stack_list.appendleft(cmd[1])
        elif cmd[0] == 'push_back' :
            stack_list.append(cmd[1])
        elif cmd[0] == 'size' :
            print(len(stack_list))
        elif cmd[0] == 'empty' :
            if len(stack_list) == 0 :
                print(1)
            else :
                print(0)
        else :
            if len(stack_list) == 0 :
                print(-1)
            else :
                if cmd[0] == 'pop_front' :
                    print(stack_list.popleft())
                elif cmd[0] == 'pop_back' :
                    print(stack_list.pop())
                elif cmd[0] == 'front' :
                    print(stack_list[0])
                else :
                    # back
                    print(stack_list[-1])
    return


if __name__ == '__main__':
    solution(int(input()))
