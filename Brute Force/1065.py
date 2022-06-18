N = int(input())
hansu = []


def search(n):

    arr = []

    for i in str(n):
        arr.append(int(i))   
    
    if len(arr) == 1:
        hansu.append(1)
    
    for i in range(1, len(arr), 1):   
        
        if (arr[i] - arr[i-1] == arr[1] - arr[0]):
           
            if (i == len(arr)-1):  
                hansu.append(1)

for n in range(1, N + 1):
    search(n)
print(len(hansu))

