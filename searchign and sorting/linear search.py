def find_element(arr, size, element, start):
    if start > size:
        return 
    else:
        if arr[start] == element:
            return start + 1
        else:
            return find_element(arr, size, element, start+1)
        
arr = [1, 4, 8, 2, 7, 9, 0]
size = len(arr)-1
element = 2
start = 0
print(f"the {element} exist in the {find_element(arr, size, element, start)}, place inside the array")