Python 3.11.0b5 (main, Jul 25 2022, 22:59:14) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def EX3_1(x):
    mylist=[]
    while x>1 :
        if x%2==0 :
            x=int(x/2)
            mylist.append(x)
        elif x%2!=0 :
            x=int(x*3+1)
            mylist.append(x)
    return len(mylist)

print(EX3_1(10))
6
