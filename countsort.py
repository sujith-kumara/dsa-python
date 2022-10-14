def countsort(arr):
    size = len(arr)
    output = [0]*size
    count = [0]*10
    
    for i in range(0,size):
        count[arr[i]] += 1
    #print(count)

    for i in range(1,10):
        count[i]+= count[i-1]
    #print(count)

    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
        #print(count)
    #print("out",output)

    for i in range(0,size):
        arr[i] = output[i]




arr = [4,2,2,8,3,3,1]
countsort(arr)
print(arr)

    