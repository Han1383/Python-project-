def EX3_5(x):
    y=0
    for i in range(0 , len(x)):
        if i < 0:
            i = i * (-1)
            y += i
        else :
            y += i
    if y == 25 :
        return True 
    else : 
        return y

