def find_difference(arr, size, start, second, target_difference):
    if second > size:
        if start > size-1:
            return 
        else:
            start += 1
            second = start + 1
            return find_difference(arr, size, start, second, target_difference)
    else:
        if abs(arr[start] - arr[second]) == target_difference:
            print([arr[start], arr[second]], end=' ')
            return find_difference(arr, size, start, second+1, target_difference)
        else:
            return find_difference(arr, size, start, second+1, target_difference)

arr = [5, 20, 3, 2, 50, 80]
size = len(arr)-1
start = 0
second = 1
target_difference = 78
find_difference(arr, size, start, second, target_difference)          