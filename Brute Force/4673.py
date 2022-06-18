not_selfnum = set()

def d(n):
    for i in str(n):
        n += int(i) 
    return n

for i in range(1, 10001):
    not_selfnum.add(d(i))

selfnum = set(range(1,10001)) - not_selfnum

for num in sorted(selfnum):
    print(num)

