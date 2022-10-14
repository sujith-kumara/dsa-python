def selectionsort(a):
    n = len(a)
    for i in range(n-1):
        ind = i
        for j in range(i+1,n):
            if a[j] < a[ind]:
                ind = j
        a[i],a[ind] = a[ind],a[i]
    print(a)

a = [76,4,3,2]
selectionsort(a)