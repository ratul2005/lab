arr = [9, 4, 1, 7, 3, 10, 2, 6, 8, 5]


for i in range(len(arr)-1):
    for j in range(len(arr)-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(*arr)            