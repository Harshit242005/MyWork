def sort_array(arr, size, start, second):
    if second > size:
        return arr
    else:
        if arr[start] > arr[second]:
            x = arr[start]
            arr[start] = arr[second]
            arr[second] = x
            return sort_array(arr, size, start, second+1)
        else:
            return sort_array(arr, size, start, second+1)
        
arr = [2, 1, 4, 7, 5]
size = len(arr)-1
start = 0
second = 1
print(sort_array(arr, size, start, second))