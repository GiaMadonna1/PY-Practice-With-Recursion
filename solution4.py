def exponent(value1, value2):
    if value2 < 0:
        print("Please enter a valid number")
    elif value1 > 50:
        print("This will break your computer")
    else:
        return value1 * exponent(value1,value2-1)
    
exponent(3,6)