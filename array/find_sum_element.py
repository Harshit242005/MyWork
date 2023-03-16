# example array = [2, 4, 5, 3, 1] find 6 answer is = [(2, 4), (1, 5)]
def find_element_sum(arr, size, start, second, target):
    if second > size:
        if start > size-1:
            return 
        else:
            start = start + 1
            second = start + 1
            return find_element_sum(arr, size, start, second, target)
    else:
        if arr[start] + arr[second] == target:
            print((arr[start], arr[second]), end=" ")
            return find_element_sum(arr, size, start, second+1, target)
        else:
            return find_element_sum(arr, size, start, second+1, target)

arr = [2, 4, 5, 3, 1]
size = len(arr)-1
start = 0
second = 1
target = 6
find_element_sum(arr, size, start, second, target)            