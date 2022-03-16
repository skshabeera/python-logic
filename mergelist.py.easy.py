l1 = [1,2,4] 
l2 = [1,3,4]
l1.extend(l2)
i=0
while i<len(l1):
    l1.sort()
    i=i+1
print(l1)
# def merge_list():
#     l1 = [1,2,4] 
#     l2 = [1,3,4]
#     l1.extend(l2)
#     i=0
#     while i<len(l1):
#         j=0
#         while j<len(l1):
#             if l1[i]>l1[j]:
#                 a=l1[j]
#                 l1[j]=l1[i]
#                 l1[i]=a
#             i+=1
#             j=j+1
#     print(l1)
# merge_list()
            