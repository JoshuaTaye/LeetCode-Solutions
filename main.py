def twoSum(arr, n):
    lst = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            if int(arr[i]) + int(arr[j]) == n:
                if i not in lst:
                    lst.append(i)
                if j not in lst:
                    lst.append(j)
    return lst


# nums = input()
nums = input().strip('[').strip(']').split(',')
target = int(input('Enter target'))
print(twoSum(nums, target))
