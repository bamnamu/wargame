def extend_gcd(a, b, s1, s2, t1, t2):
    if b==0:
        return (s1, t1)
    else:
        d=a//b
        c=a%b
        s=s1-d*s2
        t=t1-d*t2
        return extend_gcd(b, c, s2, s, t2, t)

eg=extend_gcd(13, 3, 0, 1, 1, 0)
print(eg[0]%13)