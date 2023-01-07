N = int(input())
heights = [int(input()) for i in range(N)]


stack = []
answer = 0

for height in heights:

    while stack:

        if (stack[-1] > height):
            break
        else:
            stack.pop()
        
    stack.append(height)
    answer += len(stack) - 1

print(answer)