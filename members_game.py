a = list(map(float, input().split()))
length = len(a)
total = 0
for i in range(length):
    for j in range(length):
        total = a[j] / 2
        a[j] = round(a[j], 3) / 2
        a[length - i - 1] += round(total, 3)
    print(a)
