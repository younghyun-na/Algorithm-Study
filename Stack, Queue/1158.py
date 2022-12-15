from collections import deque

n, k = map(int, input().split())

queue = deque()
answer = []

for i in range(n):   
    queue.append(i+1)

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print(str(answer).replace('[', '<').replace(']', '>'))