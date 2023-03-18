def find_majority_element(arr, size, start, second, count):
    if second > size:
        if start > size-1:
            return 
        if count > (size+1) // 2:
            return arr[start]
        else:
            count = 1
            start += 1
            second = start + 1
            return  find_majority_element(arr, size, start, second, count)
    else:
        if arr[start] == arr[second]:
            return find_majority_element(arr, size, start, second+1, count+1)
        else:
            return find_majority_element(arr, size, start, second+1, count)  

arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
size = len(arr)-1
start = 0
second = 1
count = 1
print(f"the majority element exits in the array is {find_majority_element(arr, size, start, second, count)}")             