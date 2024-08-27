def moveZeroes(nums):
    for i in range(nums):
        if i == 0:
            nums.remove(i)
            nums.append(0)

print(moveZeroes([0, 1, 0, 3, 12]))