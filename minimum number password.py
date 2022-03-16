def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    c=0
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    l=[0]*4
    for i in password:
        if i in numbers:
            l[0]+=1
        elif i in lower_case:
            l[1]+=1
        elif i in upper_case:
            l[2]+=1
        else:
            l[3]+=1
    print(n)
    for i in l:
        if i==0:
            c+=1
    if n<6:
        p=6-n
        if p<c:
            return c
        else:
            return p
    else:
        return c
print(minimumNumber(1,'9'))