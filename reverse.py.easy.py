def reverse():
    x = 123
    rev_num=0
    while x>0:
        r=x%10
        rev_num=rev_num*10+r
        x=x//10
    print(rev_num)
reverse()

