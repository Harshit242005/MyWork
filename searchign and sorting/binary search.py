def find_element(arr, start, mid, end, element):
    if element == arr[mid]:
        return mid+1
    if element > arr[mid]:
        start = mid
        mid = (start + end) // 2
        return find_element(arr, start, mid, end, element)
    if element < arr[mid]:
        end = mid
        mid = (start + end) // 2
        return find_element(arr, start, mid, end, element)
    
arr = []
for x in range(1, 11):
    arr.append(x)
start = 0
end = len(arr)-1
mid = (start + end) // 2
element = 2
print(f"the {element} is at {find_element(arr, start, mid, end, element)}")        