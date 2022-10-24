Python 3.11.0b5 (main, Jul 25 2022, 22:59:14) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def Ex1_6(x):
    '''

  Return the roman numeral version of that number.

  example:
  >>>Ex1_6example(1)
  |
  '''
    input("enter a number within the range of 1through 10:")
    if x==1:
        return("|")
    if x==2:
        return("||")
    if x==3:
        return("|||")
    if x==4:
        return("|V")
    if x==5:
        return("V")
    if x==6:
        return("V|")
    if x==7:
        return("V||")
    if x==8:
        return("V|||")
    if x==9:
        return("|X")
    if x==10:
        return("X")
    else:
        return("Error")