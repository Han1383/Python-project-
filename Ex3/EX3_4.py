def EX3_4(a,b,c):
    y= a*(2**b)
    if y % c == 0:
        return True
    else:
        return False
print(EX3_4(5,2,1))
