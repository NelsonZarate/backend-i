

def factorial(number):
    assert not isinstance(number,(str,bool,float,dict,list,tuple)), f"{type(number)} is not acceptable"
    
    if type(number) != int:
        raise TypeError("factorial of a number must be int")
    
    if(number == 0):
        return 1
    if(number < 0 ):
        raise ValueError("number must be greater than 0")
    else:
        return  number* factorial(number - 1)
   