def solution(prices):
    stack = [0]
    answer = [ i for i in range (len(prices) - 1, -1, -1)]

    for i in range(1, len(prices)):
        
        while stack and prices[stack[-1]] > prices[i]:
            index = stack.pop()
            answer[index] = i - index

        stack.append(i)
    
    return answer

