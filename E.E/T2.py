Python 3.11.0b5 (main, Jul 25 2022, 22:59:14) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def t(list):
    for x in list:
        a=list.index(x)
        b=list.index(x)+1
        p=a+b
        return p
    c=count(,)+1
    return p/c
SyntaxError: invalid syntax

def t(list):
    for x in list:
        a=list.index(x)
        b=list.index(x)+1
        p=a+b
        return p
    c=count(',')+1
    return p/c

t([2,3,4])
1
def t(x):
    x=[]
    a=0
    for i in x:
      return a+=i
    
SyntaxError: invalid syntax
def t(x):
    x=[]
    a=0
    for i in x:
      c=(a+=i)
      
SyntaxError: invalid syntax
def t(x):
    x=[]
    a=0
    for i in x:
      c=(a+i)
    return c/len(x)

t(2,3,4)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    t(2,3,4)
TypeError: t() takes 1 positional argument but 3 were given
t(x)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    t(x)
NameError: name 'x' is not defined
t(2)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    t(2)
  File "<pyshell#27>", line 6, in t
    return c/len(x)
UnboundLocalError: cannot access local variable 'c' where it is not associated with a value
t([2,3,4])
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    t([2,3,4])
  File "<pyshell#27>", line 6, in t
    return c/len(x)
UnboundLocalError: cannot access local variable 'c' where it is not associated with a value
def t(x):
    x=[]
    a=0
    for i in x:
        a+i
    return a+i/len(x)

t([2,3,4])
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    t([2,3,4])
  File "<pyshell#33>", line 6, in t
    return a+i/len(x)
UnboundLocalError: cannot access local variable 'i' where it is not associated with a value
def t(list):
    a=0
    for i in list:
        a+i
    return a+i/len(x)

t([2,3,4])
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    t([2,3,4])
  File "<pyshell#36>", line 5, in t
    return a+i/len(x)
NameError: name 'x' is not defined
def t(list):
    a=0
    for i in list:
        a+i
    return a+i/len(list)

t([2,3,4])
1.3333333333333333
def t(list):
    a=0
    for i in list:
        a+i
    return a/len(list)

t([2,3,4])
0.0
def t(list):
    a=0
    for i in list:
        a==a+i
    return a/len(list)

t([2,3,4])
0.0
def t(list):
    a=0
    for i in list:
        a=a+i
    return a/len(list)

t([2,3,4])
3.0
def v (list):
    a=list.index(len(v)/2)
    b=list.index(len(v.reverse)/2)
    if a==b:
        return a
    elif a!=b:
        return a,b

    
v([2,3,4])
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    v([2,3,4])
  File "<pyshell#57>", line 2, in v
    a=list.index(len(v)/2)
TypeError: object of type 'function' has no len()
def v (list):
    a=list.index(len(v)/2)
    list.reverse
    b=list.index(len(v)/2)
    if a==b:
        return a
    elif a!=b:
        return a,b

    
v([2,3,4])
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    v([2,3,4])
  File "<pyshell#60>", line 2, in v
    a=list.index(len(v)/2)
TypeError: object of type 'function' has no len()
def v (list):
    a=list.index(len(list)/2)
    list.reverse
    b=list.index(len(list)/2)
    if a==b:
        return a
    elif a!=b:
        return a,b

    
v([2,3,4])
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    v([2,3,4])
  File "<pyshell#63>", line 2, in v
    a=list.index(len(list)/2)
ValueError: 1.5 is not in list
def v (list):
    a=list.index((len(list)//2)+1)
    list.reverse
    b=list.index((len(list)//2)+1)
    if a==b:
        return a
    elif a!=b:
        return a,b

    
v([2,3,4])
0
def v (list):
    a=list[(len(list)//2)+1]
    list.reverse
    b=list[(len(list)//2)+1]
    if a==b:
        return a
    elif a!=b:
        return a,b

    
v([2,3,4])
4
def v (list):
    a=list[((len(list)+1)//2)+1]
    list.reverse
    b=list[((len(list)+1)//2)+1]
    if a==b:
        return a
    elif a!=b:
        return a,b

    
v([2,3,4])
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    v([2,3,4])
  File "<pyshell#72>", line 2, in v
    a=list[((len(list)+1)//2)+1]
IndexError: list index out of range
def v (list):
    a=list[(len(list)//2)+1]
    list.reverse
    b=list[(len(list)//2)+1]
    if a==b:
        return a
    elif a!=b:
        return a,b

    
def v(list):
    a=len(list)//2+1
    list.reverse
    b=len(list)//2+1
    if a==b:
        return a
    elif a!=b:
        return a,b


v([2,3,4])
2
def v(list):
    a=len(list)//2+1
    list.reverse
    b=len(list)//2+1
    if a==b:
        return list.index(a)
    elif a!=b:
        return list.index(a)and list.index(b)

    
v([2,3,4])
0
def v(list):
    a=len(list)//2+1
    list.reverse
    b=len(list)//2+1
    if a==b:
        print(list.index(a))
    elif a!=b:
        print(list.index(a)/n list.index(b))
        
SyntaxError: invalid syntax. Perhaps you forgot a comma?
def v(list):
    a=len(list)//2+1
    list.reverse
    b=len(list)//2+1
    if a==b:
        print(list.index(a))
    elif a!=b:
        print(list.index(a), /n list.index(b))
        
SyntaxError: invalid syntax
def v(list):
    a=len(list)//2+1
    list.reverse
    b=len(list)//2+1
    if a==b:
        print(list.index(a))
    elif a!=b:
        print(list.index(a),list.index(b))

        
v([2,3,4])
0
def v(list):
    a=len(list)//2+1
    list.reverse
    b=len(list)//2+1
    if a==b:
        print(list[a])
    elif a!=b:
        print(list[a],list[b])

        
v([2,3,4])
4
def v(list):
    a=len(list)//2
    list.reverse
    b=len(list)//2
    if a==b:
        print(list[a])
    elif a!=b:
        print(list[a],list[b])

        
v([2,3,4])
3


v([1,2,3,4])
3
def v(list):
    a=len(list)//2
    list.reverse
    b=len(list)//2+1
    if a==b:
        print(list[a])
    elif a!=b:
        print(list[a],list[b])

        
v([1,2,3,4])
3 4
def v(list):
    a=len(list)//2
    list.reverse
    b=len(list)//2-1
    if a==b:
        print(list[a])
    elif a!=b:
        print(list[a],list[b])

        
v([1,2,3,4])
3 2
v([9,8,7])
8 9
def v(list):
    if (len(list))%2==0:
        a=len(list)//2
        print(list[a])
    elif (len(list))%2!=0 :
        a=len(list)//2
        b=(len(list)//2)-1
        print(list[a],list[b])

        
v([1,2,3,4])
3
def v(list):
    if (len(list))%2!=0:
        a=len(list)//2
        print(list[a])
    elif (len(list))%2==0 :
        a=len(list)//2
        b=(len(list)//2)-1
        print(list[a],list[b])

        
v([1,2,3,4])
3 2
v([9,8,7])
8
def e(listA,listB):
    print(listA,listB)

    
e([1,2,3],[a,b,c])
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    e([1,2,3],[a,b,c])
NameError: name 'a' is not defined

e([1,2,3],[4,5,6,7])
[1, 2, 3] [4, 5, 6, 7]
def e(listA,listB):
    for x in listB :
        listA.append(x)
    print(listA)

    
e([1,2,3],[4,5,6,7])
[1, 2, 3, 4, 5, 6, 7]
def i(listA,listB)
SyntaxError: expected ':'
def i(listA,listB):
    c=[]
    for x in listA:
        if x in listB:
            c.append(x)

            
def i([1,2,3,4],[2,4,5])
SyntaxError: invalid syntax
def i(listA,listB):
    c=[]
    for x in listA:
        if x in listB:
            c.append(x)
    print(c)

    
i([1,2,3,4],[2,4,5])
[2, 4]
def o(*arg):
    a=list(*arg)
    print(a)

    
o(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    o(1,2,3,4,5)
  File "<pyshell#154>", line 2, in o
    a=list(*arg)
TypeError: list expected at most 1 argument, got 5
o(1)
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    o(1)
  File "<pyshell#154>", line 2, in o
    a=list(*arg)
TypeError: 'int' object is not iterable
o(*1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    o(*1,2,3,4,5)
TypeError: Value after * must be an iterable, not int
o(*a,b)
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    o(*a,b)
NameError: name 'a' is not defined
def o(*args):
    a=list(*args)
    print(a)

    
o(*1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    o(*1,2,3,4,5)
TypeError: Value after * must be an iterable, not int
o(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    o(1,2,3,4,5)
  File "<pyshell#160>", line 2, in o
    a=list(*args)
TypeError: list expected at most 1 argument, got 5
o(1,2,3,4,5,*args)
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    o(1,2,3,4,5,*args)
NameError: name 'args' is not defined
def o (a):
    input('please enter your objects:()')
    print(list(a))

    
o(a)
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    o(a)
NameError: name 'a' is not defined
o(a)
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    o(a)
NameError: name 'a' is not defined
0(1)
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    0(1)
TypeError: 'int' object is not callable
def os (a):
    print(list(a))

    
os(1,2)
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    os(1,2)
TypeError: os() takes 1 positional argument but 2 were given
def os (a):
    c=list(a)
    print(c)

    
os(1,2)
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    os(1,2)
TypeError: os() takes 1 positional argument but 2 were given
def os (*a):
    c=list(a)
    print(c)

    
os(1,2)
[1, 2]
