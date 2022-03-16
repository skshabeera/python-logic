def median():
    nums1 = [1,2]
    nums2 = [3,4]
    nums1.extend(nums2)
    i=0
    sum=0
    c=0
    while i<len(nums1):
        sum=sum+nums1[i]
        c=c+1
        a=sum/c
        i=i+1
    print(a)
median()

