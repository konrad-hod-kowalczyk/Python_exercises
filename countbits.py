def countBits(n):
    b=0
    while n>=0:
        if n%2==1:
            b = b+n%2
        n=int(n/2)
        if n==0:
            break
    return b
