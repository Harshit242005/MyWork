def get_new_length(arr, size, start, second):
    if second > size:
        if start > size-1:
            return size+1
        else:
            start = start + 1
            second = start + 1
            return get_new_length(arr, size, start, second)
        
    else:
        if arr[start] == arr[second]:
            arr.pop(second)    
            size = size-1
            return get_new_length(arr, size, start, second+1)
        else:
            return get_new_length(arr, size, start, second+1)
        
arr = [1, 1, 3, 5, 5, 7, 7]
size = len(arr)-1
start = 0
second = 1
print(f"the lenght of the array after removing the duplicates is : {get_new_length(arr, size, start, second)}")        