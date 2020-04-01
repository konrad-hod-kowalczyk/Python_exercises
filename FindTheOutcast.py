def find_outlier(integers):
    p = 0
    n = 0
    number = 0
    i=0
    for j in integers:
        if int(integers[i]/2)==integers[i]/2: 
            p = p+1
        else: 
            n = n+1
        i=i+1
    i=0
    if p>n:
        for j in integers:
            if int(integers[i]/2)!=integers[i]/2:
                number=integers[i];
                break
            i=i+1
    else: 
        for k in integers:
            if int(integers[i]/2)==integers[i]/2:
                number=integers[i];
                break
            i=i+1
    return number
