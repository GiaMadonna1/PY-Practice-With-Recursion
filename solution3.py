def f_sequence(num):
    if num < 0:
        return num
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    
    else:
        return(f_sequence(num-1) + f_sequence(num-2))



f_sequence(6)



