stack = []

def solution(arr):
    
    for num in arr:
        
        if not stack:
            stack.append(num)
            
        elif num != stack[-1]:
            stack.append(num)
        
    return stack
