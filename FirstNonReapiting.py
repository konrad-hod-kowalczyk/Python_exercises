def first_non_repeating_letter(string):
    v=len(string)
    fad=""
    for i in range(v):
        for j in range(i+1,v):
            if string[i].isupper():
                if string[i]==string[j].upper():
                    fad=fad+string[i]
            else:
                if string[i]==string[j].lower():
                    fad=fad+string[i]
    y=len(fad)
    for i in range(v):
        b=0
        for j in range(y):
            if string[i]==fad[j]:
                b=b+1
        if b==0:
            return string[i]
    return ""
