# find the majority element which has occured more than n/2 times where n is the size of the array
def find_major(arr, size, start, second, count):
    if second > size:
        if count > size // 2:
            return arr[start]
        if start > size-1:
            return 
        else:
            count = 1
            start += 1
            second = start + 1
            return find_major(arr, size, second, count)
        
    else:
        if arr[start] == arr[second]:
            return find_major(arr, size, start, second+1, count+1)
        else:
            return find_major(arr, size, start, second+1, count)

arr = [2, 1, 2, 2, 3, 2, 4, 2]
size = len(arr)-1
start = 0
second = 1
count = 1
print(f"the majority element is {find_major(arr, size, start, second, count)}")            