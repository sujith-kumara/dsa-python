def insertionsort(a):
    n = len(a)
    for i in range(1,n):
        value = a[i]
        j = i-1
        while j>=0 and value < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = value
    print(a)
a = [9,8,5,4,3]
insertionsort(a)