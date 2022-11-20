def EX3_6(list):
    y=max(list)
    x=min(list)
    z = y-x 
    if z in list :
        return (':)')
    elif len(list) == 0:
        return(':/')
    else:
        return(':(')


print(EX3_6([1,2,5,8,3,9]))
