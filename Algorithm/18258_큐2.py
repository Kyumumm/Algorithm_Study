from collections import deque
import sys

#first_try 는 08_queue.py 에 나와있는 그대로 구현 => 시간초과

input = sys.stdin.readline

n = int(input())
stack = deque()


def push(x):
    stack.append(x)


def pop():
    if not stack:
        return -1
    return stack.popleft()


def size():
    return len(stack)


def empty():
    if not stack:
        return 1
    return 0


def front():
    if not stack:
        return -1
    return stack[0]


def back():
    if not stack:
        return -1
    return stack[-1]


for _ in range(n):
    command = input().split()
    if 'push' in command:
        push(command[1])
    elif 'front' in command:
        print(front())
    elif 'back' in command:
        print(back())
    elif 'size' in command:
        print(size())
    elif 'empty' in command:
        print(empty())
    else:
        print(pop())

# 데크(deque)의 개념
# 보통 큐(queue)는 선입선출(FIFO) 방식으로 작동한다. 반면, 양방향 큐가 있는데 그것이 바로 데크(deque)다.

# 즉, 앞, 뒤 양쪽 방향에서 엘리먼트(element)를 추가하거나 제거할 수 있다.

# 데크는 양 끝 엘리먼트의 append와 pop이 압도적으로 빠르다.

# 컨테이너(container)의 양끝 엘리먼트(element)에 접근하여 삽입 또는 제거를 할 경우, 일반적인 리스트(list)가 이러한 연산에 O(n)이 소요되는 데 반해, 데크(deque)는 O(1)로 접근 가능하다.


# 데크(deque), 언제, 왜 써야 하는가?
# 요약하자면, 데크(deque)는 스택처럼 사용할 수도 있고, 큐 처럼 사용할 수도 있다.

# 시작점의 값을 넣고 빼거나, 끝 점의 값을 넣고 빼는 데 최적화된 연산 속도를 제공한다.

# 즉, 대부분의 경우에 데크(deque)는 리스트(list)보다 월등한 옵션이다.

# 데크는 특히 push/pop 연산이 빈번한 알고리즘에서 리스트보다 월등한 속도를 자랑한다.

# deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
# deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
# deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
# deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
# deque.remove(item): item을 데크에서 찾아 삭제한다.