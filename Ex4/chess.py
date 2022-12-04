'''
هانا اکبرحسینی
4012061006
'''
H=['A','B','C','D','E','F','G','H','a','b','c','d','e','f','g','h']
A=['1','2','3','4','5','6','7','8']
Hk=input('please enter horizontal position of the knight(a,b,c,d,e,f,g,h): ')
Ak=input('please enter vertical position of the knight(1,2,3,4,5,6,7,8):')
Hb=input('please enter horizontal position of the bishop(a,b,c,d,e,f,g,h):')
Ab=input('please enter vertical position of the bishop(1,2,3,4,5,6,7,8):')
if Hk not in H:
    print('horizontal input is not a proper letter')
if Hk.isalpha()==False :
    print ('horizontal input is not a letter')
if Hb not in H:
    print('horizontal input is not a proper letter')
if Hb.isalpha()==False :
    print ('horizontal input is not a letter')
if Ak not in A:
    print('vertical input for knight is not a proper number')
if Ak.isnumeric()==False :
    print('vertical input is not a number')
if Ab not in A:
    print('vertical input is not a proper number')
if Ab.isnumeric()==False :
    print('vertical input for bishop is not  a number')
if Hb==Hk and Ab==Ak:
    print('They cant be in the same square')
else:
    in1=(H.index(Hb))+1
    in2=(H.index(Hk))+1 
    in3=(A.index(Ab))+1
    in4=(A.index(Ak))+1
    if in1>8:
        in1=in1-8
    if in2>8:
        in2=in2-8
    if in1-in3==in2-in4 :
        print ('bishop can attack knight')
    elif in1+in3==in2+in4 :
        print ('bishop can attack knight')
    elif in2+2==in1 and in4+1==in3:
        print ('knight can attack bishop')
    elif in2+2==in1 and in4+-1==in3:
        print ('knight can attack bishop')
    elif in2-2==in1 and in4+1==in3:
        print ('knight can attack bishop')
    elif in2-2==in1 and in4-1==in3:
        print ('knight can attack bishop')
    elif in2+1==in1 and in4+2==in3:
        print ('knight can attack bishop')
    elif in2+1==in1 and in4-2==in3:
        print ('knight can attack bishop')
    elif in2-1==in1 and in4+2==in3:
        print ('knight can attack bishop')
    elif in2-1==in1 and in4-2==in3:
        print ('knight can attack bishop')
    else :
          print ('neither of them can attack each other')