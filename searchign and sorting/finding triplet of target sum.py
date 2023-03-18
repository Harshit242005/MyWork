def get_the_triplet(arr, size, start, second, third, target):
    if third > size:
        if second > size-1:
            if start > size-2:
                return 
            else:
                start += 1
                second = start + 1
                third = second + 1
                return get_the_triplet(arr, size, start, second, third, target)
        else:
            second += 1
            third = second + 1
            return get_the_triplet(arr, size, start, second, third, target)
    else:
        if arr[start] + arr[second] + arr[third]  == target:
            return [arr[start],  arr[second],  arr[third]]  
        if arr[start] + arr[second] + arr[third]  == target+1:
             return [arr[start],  arr[second],  arr[third]]
        if arr[start] + arr[second] + arr[third]  == target-1:
             return [arr[start],  arr[second],  arr[third]]    
        else:
            return get_the_triplet(arr, size, start, second, third+1, target)  

arr = [2, 1,-1, -4, 3, 0]
size = len(arr)-1
start = 0
second = 1
third = 2
target = 5
print(f"the triplet value whose sum is close to {target} is {get_the_triplet(arr, size, start, second, third, target)}")         