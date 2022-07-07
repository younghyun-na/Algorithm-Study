N = int(input())

count = 0

while (True):

    if (N % 5 != 0):
        N -= 3
        count += 1

    elif (N % 5 == 0):
        count += N // 5
        N %= 5
        print(count)
        break

    if (N < 0):
        print(-1)
        break







    





    



