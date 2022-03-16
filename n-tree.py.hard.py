def flatted_list():
    root = [1,"null",3,2,4,"null",5,6]
    i=0
    b=[]
    s=[]
    while i<len(root):
        if root[i]=="null":
            s.append(b)
            b=[]
        else:
            b.append(root[i])
        i=i+1
    s.append(b)
    print(s)
flatted_list()


