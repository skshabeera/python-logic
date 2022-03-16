nums = [1,1,2]
i=0
# j=1
list=[]
while i<len(nums):
    if nums[i] not in list:
        list.append(nums[i])
    