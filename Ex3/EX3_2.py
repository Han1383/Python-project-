Python 3.11.0b5 (main, Jul 25 2022, 22:59:14) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

def EX3_2(x):
    set_i=[]
    for z in range (0,len(x)-1):
     y=x[z]*x[z+1]
     set_i.append(y)
    set_i.sort(reverse=True)
    return set_i[0]

EX3_2([3,6,-2,-5,7,3])
21
