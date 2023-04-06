def check_string( base, search):
    return search in base



def all_caps(animals):
    if len(animals) == 0:
        return 
    else:
        return (f"{animals[0].upper()}{all_caps(animals[1:])}")


print(all_caps(animals=['koalas', 'monkeys', 'bears', 'dogs']))