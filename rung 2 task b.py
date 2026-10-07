nums=[3, 3, 9, 1, 1]
def centered_average(nums):
    nums=nums[:]
    nums.remove(max(nums))
    nums.remove(min(nums))
    count=0
    total=0
    for i in nums:
        total=total+i
        count=count+1
    return total//count
a=centered_average(nums)
print (a)
print (nums)