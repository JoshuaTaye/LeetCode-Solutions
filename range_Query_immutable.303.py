class NumArray:
    def __init__(self, nums):
        self.numArray = nums
        self.nums = nums
        ps = [self.nums[0]]
        for i in range(1, len(self.nums)):
            ps.append(ps[i - 1] + self.nums[i])
        self.ps = ps
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.ps[right]
        return self.ps[right] - self.ps[left - 1]

# Your NumArray object will be instantiated and called as such:
nums = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
obj = NumArray(nums[0][0])
print(obj.sumRange(nums[1][0],nums[1][1]))
print(obj.sumRange(nums[2][0],nums[2][1]))
print(obj.sumRange(nums[3][0],nums[3][1]))

