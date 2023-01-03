string = input()
bomb = input()

stack = []

for char in string:

    stack.append(char)

    if "".join(stack[-len(bomb):]) == bomb:
        for i in range(len(bomb)):
            stack.pop()

if stack:
    print("".join(stack))

else:
    print("FRULA")


