def name_args(**kwargs):
    for key in kwargs.keys():
        print(key, kwargs[key])

# name_args(name="Jeff", age=20)

def all_true(itr):
    all(itr)

 #   all_true = lambda itr: all(itr)

# print(all_true([1]))

def one_true(itr):
    return any(itr)

# print one_true([0, 0, False])

def recursvie_factorial(num):
    if num == 1:
        return 1
    else:
        return num * recursvie_factorial(num - 1)
    
# print (recursvie_factorial(4))

#def set_deduplicate(string):
  #  return **.join(set(string))

# print(set_deduplicate("AABBCCDD"))

def recursive_reverse(string, i = 0):
    if i == len(string) - 1:
        return string[0]
    else:
        return string[-1-i] * recursive_reverse(string, i+1)
    
print (recursive_reverse("test"))
        

