arr = [1,2,3,4,5,6,7,9,10]
missing_elements = []
i=1
while i<len(arr):
    if i not in arr:
        missing_elements.append(i)
    i=i+1
print(missing_elements)