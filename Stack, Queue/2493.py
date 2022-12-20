N = int(input())
heights = list(map(int,input().split()))

stack = []
answer = []

for i in range(N):   

    while stack:

        if stack[-1][1] > heights[i]:   
            answer.append(stack[-1][0] + 1)
            break

        else:         
            stack.pop()
                
    if not stack:
        answer.append(0)
        
    stack.append([i, heights[i]])

print(" ".join(map(str, answer)))

     
