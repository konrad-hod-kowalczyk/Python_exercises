def expanded_form(num):
    i=""
    n=num
    k=0
    while(n>0):
        n=int(n/10)
        k=k+1
    if num%10!=0:
        i=str(num%10)+i
    n=num
    n=int(n/10)
    p=0
    j=1
    while(n>0):
        p=n%10
        c=j
        while(c>0):
            if p==0:
                break
            p=str(p)+"0"
            c=c-1
        if p!=0:
            if i!="":
                i=p+" + "+i
            if i=="":
                i=p
        n=int(n/10)
        j=j+1
    return i
