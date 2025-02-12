def moveZeroes(nums):
    placeholder = 0
    seeker = 0
    while seeker < len(nums) and placeholder < len(nums) - 1:
        while placeholder < len(nums) - 1 and nums[placeholder] != 0:
            placeholder += 1
        print(placeholder)
        if placeholder == len(nums) - 1:
            return
        if nums[seeker] != 0:
            print("seeker",seeker)
            if seeker > placeholder:
                nums[seeker], nums[placeholder] = nums[placeholder], nums[seeker]
        seeker += 1
    return nums

print(moveZeroes([4,2,4,0,0,3,0,5,1,0]))