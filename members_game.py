a = list(map(int,input().split()))
length = len(a)
total = 0
for i in range(length):
    for j in range(length):
        total = a[j]/2
        a[j] = a[j]/2
        a[length-i-1] += total
    print(a)
