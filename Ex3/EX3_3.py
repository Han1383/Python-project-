Python 3.11.0b5 (main, Jul 25 2022, 22:59:14) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def Ex3_3(x):
    '''
destination1=n*2+e*3
destination2=w*4+n*3
    '''
    q=x.count("n")
    p=x.count("w")
    z=x.count("s")
    t=x.count("e")
    if q-z==2 and t-p==3:
        return True
    elif p-t==4 and q-z==3 :
        return True
    else :
        return False

    

Ex3_3(["s","e","e","n","n","e","n"])
True
