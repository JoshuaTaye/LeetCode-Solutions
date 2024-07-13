def removeDuplicates(arr):
    new_arr = [None] * len(arr)
    i = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            arr.remove(arr[i])
            continue
        else:
            i += 1
    return arr


# arr = input()
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
