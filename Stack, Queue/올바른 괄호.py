def solution(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    
    if stack:
        return False
    
    return True