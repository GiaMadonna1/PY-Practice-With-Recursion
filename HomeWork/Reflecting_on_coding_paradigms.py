'''
Implement a function that will flatten and sort an array of integers in 
ascending order, and which adheres to a functional programming paradigm.

'''

def flatten_sort_dict(dictionary):
    flattened = {}
    for key in dictionary.keys():
        if isinstance(dictionary[key], dict):
            for inner_key, inner_value in dictionary[key].items():
                flattened.update({key + "," + inner_key: inner_value })
                
        else:
            flattened.update({key: dictionary[key]})
    return sorted(flattened)

print(flatten_sort_dict({'a': 50, 'b': {'x': 2, 'y': 3}, 'c': 4}))