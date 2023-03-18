# in this approach the jumper can also entangled itself to the loop created by the array
def number_of_jumps(arr, size, start, count):
    if start > size or start == size:
        return count 
    else:
        start = arr[start] + start
        count += 1
        return number_of_jumps(arr, size, start, count)
arr = [1, 2, 3, 4, 5, 6, 7, 7, 8]
size = len(arr)-1
start = 0
count = 1
print(f"the number of jumps in the given {arr} is {number_of_jumps(arr, size, start, count)}")    