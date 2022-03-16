def removing_element():
    nums = [0,1,2,2,3,0,4,2] 
    i=0
    c=0
    list=[]
    while i<len(nums):
        if nums[i]==2:
            list.append("-")
        else:
            list.append(nums[i])
            c=c+1
        i=i+1
    print(c)
removing_element()

    



