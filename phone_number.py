def create_phone_number(n):
    x = ""
    i=0
    for number in n: #simple program taking a list of numbers and writing it into american phone number style, in particular places in number besides adding the number from list it also adds special character
        if i==0:
            x=x+"("
        if i==2:
            x=x+") "
        if i==5:
            x=x+"-"
        x=x+str(n[i])
        i=i+1
    return x
