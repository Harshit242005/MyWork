def find_combination(arr, size, start, second, target):
    if second > size:
        if start > size-1:
            return 
        else:
            start = start + 1
            second = start + 1
            return find_combination(arr, size, start, second, target)
    else:
        if arr[start] + arr[second] == target:
            print([arr[start], arr[second]], end=" ")  
            return find_combination(arr, size, start, second+1, target)
        else:
            return find_combination(arr, size, start, second+1, target)

arr = [1, 3, 6, 4, 5, 8, 0]
size = len(arr)-1
start = 0
second = 1
target = 9
find_combination(arr, size, start, second, target)  