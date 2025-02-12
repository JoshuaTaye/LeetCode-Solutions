def mergeSorted(arr1, arr2):
    l = 0
    r = 0
    arr3 = []
    arr1.append(float("inf"))
    arr2.append(float("inf"))
    while l < len(arr1) and r < len(arr2):
        if arr1[l] < arr2[r]:
            arr3.append(str(arr1[l]))
            l += 1
        else:
            arr3.append(str(arr2[r]))
            r += 1
    arr3.pop()
    return " ".join(arr3)

x = list(map(int, input().split()))
ar1 = list(map(int, input().split()))
ar2 = list(map(int, input().split()))

print(mergeSorted(ar1, ar2))