arr = [10, 20, 5, 8, 30, 25]

def lsearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

x = lsearch(arr, 8)
print(x)
