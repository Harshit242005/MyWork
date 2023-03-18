def find_duplcate(arr, size, start, second):
    if second > size:
        if start > size-1:
            return 
        else:
            start += 1
            second = start + 1
            return find_duplcate(arr, size, start, second)
    else:
        if arr[start] == arr[second]:
            return arr[start]
        else:
            return find_duplcate(arr, size, start, second+1)

arr = [1, 3, 4, 2, 2]
size = len(arr)-1
start = 0
second = 1
print(f"the duplicate in the {arr} is {find_duplcate(arr, size, start, second)}")         