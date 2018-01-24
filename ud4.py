def split_string(source,splitlist):
    output=[]
    atsplit=True
    for c in source:
        if c in splitlist:
            atsplit=True
        else:
            if atsplit:
                output.append(c)
                atsplit=False
            else:
                output[-1]=output[-1]+c
    return output
out=split_string('this is-a, lion!oh',",-!")
print out
