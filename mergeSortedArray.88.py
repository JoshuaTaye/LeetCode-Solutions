def merge(nums1, m, nums2):
    x = len(nums1) - m
    while x > 0:
        if 0 in nums1:
            nums1.remove(nums1[-1])
        x -= 1
    i = 0
    while i < (len(nums2)):
        g = False
        j = 0
        while j < (len(nums1)):
            if nums2[i] <= nums1[j]:
                g = True
                nums1.insert(j, nums2[i])
                break
            else:
                j += 1
        if not g:
            nums1.append(nums2[i])
        i += 1
    print(nums1)

print(merge([1,2,3,0,0,0], 3, [2, 5, 6], 3))