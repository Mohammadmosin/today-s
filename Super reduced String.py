def superReducedString(s):
    b=''
    c = 0

    k = s
    i=0
    while i<len(s):
        if i < len(s) - 1:
            if s[i] == s[i + 1]:
                c = 1
                s = s[0:i] + s[i + 2:]
        i+=1

    if c == 1:
        k = (superReducedString(s))
    else:
        if len(k) > 0:
            return k
        else:
            return 'Empty String'
    return k
print((superReducedString('aaabccddd')))