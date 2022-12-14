Python 3.11.0b5 (main, Jul 25 2022, 22:59:14) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def num(n):
    B=alist(range(n))
print(B)
SyntaxError: invalid syntax
def num(n):
    B=alist(range(n))
print(B)
def num(n):
    n=list(renge(n))
print (n)
SyntaxError: invalid syntax

def num(n):
    n=list(range(n))
    print(n)

    
num(30)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
def numB(m,n):
    s=list(range(m,n))
    print(s)

    
numB(2,22)
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
def numZ(m,n):
    a=list(range(m,n) or range(n,m))
    b=[]
    for x in a:
        if x%2==0:
           print(b.append('x'))
    print(b)

    
numZ(90,80)
None
None
None
None
None
['x', 'x', 'x', 'x', 'x']
def numZ(m,n):
    a=list(range(m,n) or range(n,m))
    b=[]
    for x in a:
        if x%2==0:
           print(b.append(x))
    print(b)

    
numZ(80,90)
None
None
None
None
None
[80, 82, 84, 86, 88]
def numZ(m,n):
    a=list(range(m+1,n) or range(n+1,m))
    b=[]
    for x in a:
        if x%2==0:
           return(b.append(x))
    print(b)

    
numZ(80,90)
numZ(90,80)

def numZ(m,n):
    a=list(range(m+1,n) or range(n+1,m))
    b=[]
    for x in a:
        if x%2==0:
           print(b.append(x))
    print(b)

    
numZ(80,90)
None
None
None
None
[82, 84, 86, 88]
def numZ(m,n):
    a=list(range(m+1,n) or range(n+1,m))
    b=[]
    for x in a:
        if x%2==0:
           return(b.append(x))
    print(b)

    
numZ(8,20)
def numZ(m,n):
    a=list(range(m+1,n) or range(n+1,m))
    b=[]
    for x in a:
        if x%2==0:
          b=b.append(x)
         return b
    print(b)
    
SyntaxError: unindent does not match any outer indentation level

def numZ(m,n):
    a=list(range(m+1,n) or range(n+1,m))
    b=[]
    for x in a:
        if x%2==0:
          b=b.append(x)
          return b
    print(b)

    

numZ(8,20)
def numZ(m,n):
    a=list(range(m+1,n) or range(n+1,m))
    b=[]
    for x in a:
        if x%2==0:
          b=b.append(x)
   return b
SyntaxError: unindent does not match any outer indentation level

def numZ(m,n):
    a=list(range(m+1,n) or range(n+1,m))
    b=[]
    for x in a:
        if x%2==0:
          b=b.append(x)
        return b

    
numZ(8,20)
[]
def numZ(m,n):
    a=list(range(m+1,n) or range(n+1,m))
    b=[]
    for x in a:
        if x%2==0:
          b==b.append(x)
        return b

    
numZ(8,20)
[]
def numZ(m,n):
    a=list(range(m+1,n) or range(n+1,m))
    b=[]
    for x in a:
        if x%2==0:
          b==b.append(x)
        print(b)

        
numZ(8,20)
[]
[10]
[10]
[10, 12]
[10, 12]
[10, 12, 14]
[10, 12, 14]
[10, 12, 14, 16]
[10, 12, 14, 16]
[10, 12, 14, 16, 18]
[10, 12, 14, 16, 18]
def numZ(m,n):
    a=list(range(m+1,n) or range(n+1,m))
    b=[]
    for x in a:
        if x%2==0:
          b.append(x)
        print(b)

        
numZ(8,20)
[]
[10]
[10]
[10, 12]
[10, 12]
[10, 12, 14]
[10, 12, 14]
[10, 12, 14, 16]
[10, 12, 14, 16]
[10, 12, 14, 16, 18]
[10, 12, 14, 16, 18]
def numZ(m,n):
    a=list(range(m+1,n) or range(n+1,m))
    b=[]
    for x in a:
        if x%2==0:
          b.append(x)
        elif x not in a :
            print(b)

            

numZ(8,20)
def numZ(m,n):
    a=list(range(m+1,n) or range(n+1,m))
    b=[]
    for x in a:
        if x%2==0:
          b.append(x)
    print(b)

    
numZ(8,20)
[10, 12, 14, 16, 18]
def five(x)
SyntaxError: expected ':'
def five(x):
    x=5*range(20)

    
five(x)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    five(x)
NameError: name 'x' is not defined
numZ(20,8)
[10, 12, 14, 16, 18]
def five(x):
    a=list(range(x))
    b=5*a

    
five(10)
def five(x):
    a=list(range(x))
    b=5*a
    print(b)

    
five(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def five(x):
    a=list(range(x))
    for s in a:
        print(s*5)

        
five(10)
0
5
10
15
20
25
30
35
40
45
def five(x):
    a=list(range(x))
    b=[]
    for s in a:
        b.append(s*5)
        print(b)

        
five(10)
[0]
[0, 5]
[0, 5, 10]
[0, 5, 10, 15]
[0, 5, 10, 15, 20]
[0, 5, 10, 15, 20, 25]
[0, 5, 10, 15, 20, 25, 30]
[0, 5, 10, 15, 20, 25, 30, 35]
[0, 5, 10, 15, 20, 25, 30, 35, 40]
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
def five(x):
    a=list(range(x))
    b=[]
    for s in a:
        b.append(s*5)
    print(b)

    
five(10)
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
def mag(n):
    a=list(range(n+1))
    b=[]
    for x in a:
        if n%a==0:
            b.append(a)
    print(b)

    
mag(7)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    mag(7)
  File "<pyshell#103>", line 5, in mag
    if n%a==0:
TypeError: unsupported operand type(s) for %: 'int' and 'list'
def mag(n):
    a=list(range(n+1))
    b=[]
    for x in a:
        if n%x==0:
            b.append(a)
    print(b)

    
mag(8)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    mag(8)
  File "<pyshell#106>", line 5, in mag
    if n%x==0:
ZeroDivisionError: integer modulo by zero

def mag(n):
    a=list(range(1,n+1))
    b=[]
    for x in a:
        if n%x==0:
            b.append(a)
    print(b)

    
mag(8)
[[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]]
def mag(n):
    a=list(range(1,n+1))
    b=[]
    for x in a:
        if n%x==0:
            b.append(x)
    print(b)

    
mag(8)
[1, 2, 4, 8]
