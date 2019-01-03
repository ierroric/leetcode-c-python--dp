class NumArray:

    def __init__(self, nums):
    """
    :type nums: List[int]
    """
    self.sumlist = []
    self.sumlist = nums
    i = 1
    while (i < len(nums)):
    	self.sumlist[i] = self.sumlist[i-1] + self.sumlist[i]
    	i+= 1

def sumRange(self, i, j):
    """
    :type i: int
    :type j: int
    :rtype: int
    """
    if i == 0:
    	return self.sumlist[j]
    else:
    	return (self.sumlist[j] - self.sumlist[i-1])
    
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
