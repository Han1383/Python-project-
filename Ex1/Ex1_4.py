Python 3.11.0b5 (main, Jul 25 2022, 22:59:14) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def Ex1_4(x):
    '''

  return the day that relates to the number.

  example:
  >>>Ex1_4(2)
  Tuesday

  '''
    input("enter a number in range of 1 through 7:")
    if x==1:
        return("Monday")
    if x==2:
        return ("Tuesday")
    if x==3:
        return ("Wednesday")
    if x==4:
        return("Thursday")
    if x==5:
        return("Friday")
    if x==6:
        return("Saturday")
    if x==7:
        return("Sunday")
    else:
        return("Error")
