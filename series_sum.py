def series_sum(n):
    if n>0:
        m = 4
        sum=1
        i=1
        while i < n:
            sum = sum+1/m
            m=m+3
            i=i+1
        zwrot = "%.2f" % round(sum,2)
        return str(zwrot)
    else:
        return "%.2f" % n
