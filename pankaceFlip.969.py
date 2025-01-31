def pancakeFlip(arr):
    pointers = []
    for i in range(10):
        pointer  = 0
        while pointer < len(arr)-1:
            if arr[pointer] > arr[pointer + 1]:
                if pointer == 0:
                    print(arr)
                    print("yes")
                    arr.reverse()
                    print(arr)
                else:
                    arr = reversed(arr[:pointer+1]) + arr[pointer+1:]
                pointers.append(pointer)
            pointer += 1
            print(arr)
    return arr
    print(reversed(arr))

print(pancakeFlip([3, 2, 4, 1]))