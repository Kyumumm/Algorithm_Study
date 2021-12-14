from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
stack = list()


def push(X):
    stack.append(X)


def pop():
    if not stack:
        return -1
    return stack.pop()


def size():
    return len(stack)


def empty():
    if not stack:
        return 1
    else:
        return 0


def top():
    if not stack:
        return -1
    return stack[-1]


for _ in range(n):
    command = input().split()
    if "push" in command:
        push(command[1])
    elif "pop" in command:
        print(pop())
    elif "size" in command:
        print(size())
    elif "empty" in command:
        print(empty())
    elif "top" in command:
        print(top())

