def sum(a,b):
    s1=" "
    s2=" "
    i=1
    while i<=len(l1):
        s1=s1+str(l1[-i])
        s2=s2+str(l2[-i])
        i=i+1
    sum=str(s1)+str(s2)
    print(sum)
    a=int(s1)+int(s2)
    b=str(a)
    i=1
    l=[]
    while i<=3:
        c=b[-i]
        d=int(c)
        l.append(d)
        i=i+1
    print(l)
l1 = [2,4,3]    
l2= [5,6,4]
sum(l1,l2)


        

    
