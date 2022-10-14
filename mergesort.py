def mergesort(list1,l,r):
    if l >= r:
        return
    middle = (l+r)//2
    mergesort(list1,l,middle)
    mergesort(list1,middle+1,r)
    merge(list1,l,r,middle)
def merge(list1,l,r,middle):
    left = list1[l:middle+1]
    right = list1[middle+1:r+1]
    i = 0
    j = 0
    k = l
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            list1[k] = left[i]
            i += 1
        else:
            list1[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        list1[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        list1[k] = right[j]
        j += 1
        k += 1
    


list1 = [9,4,3,2,1,10,89,35,45,3,7]
mergesort(list1,0,len(list1)-1)
print(list1)