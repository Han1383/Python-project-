Python 3.11.0b5 (main, Jul 25 2022, 22:59:14) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def Ex1_5(x):
    '''

  classify the age given.

  example:
  >>>Ex1_5(0.5)
  Infant
  '''
    input("enter an age")
    if x<=1:
        return("Infant")
    if x>1 and x<13:
        return("child")
    if x>=13 and x<20:
        return ("teenager")
    if x>=20:
        return("Adult")
    else:
        return ("Error")