def bubblesort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    print(a)

a = [7,6,5,4,3,2,1]
bubblesort(a)