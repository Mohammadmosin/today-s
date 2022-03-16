#You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

#The first kangaroo starts at location  and moves at a rate of  meters per jump.
#The second kangaroo starts at location  and moves at a rate of  meters per jump.
#You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.


def kangaroo(x1, v1, x2, v2):
    c=0
    if x1>x2:
        c=1
    else:
        c=2
    while x1!=x2:
        if x1>x2 and c==1 and v1<v2:
            x1=x1+v1
            x2=x2+v2
        elif x1<x2 and c==2 and v1>v2:
            x1=x1+v1
            x2=x2+v2
        else:
            return "NO"

    return "YES"

kangaroo(0,2,5,3)