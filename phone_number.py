def create_phone_number(n):
    x = ""
    i=0
    for number in n:
        if i==0:
            x=x+"("
        x=x+str(n[i])
        if i==2:
            x=x+") "
        if i==5:
            x=x+"-"
        i=i+1
    return x