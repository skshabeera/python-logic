list=[[1,4,5],[1,3,4],[2,6]]
list1=[]
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        list1.append(list[i][j])
        j=j+1
    i=i+1
    list1.sort()
print(list1)