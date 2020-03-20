def perimeter(n):
    square=2;
    r=[1,1]
    for i in range(2,n+1):
        r.append(r[i-1]+r[i-2])
        square=square+r[i]
    square = square*4
    return square
