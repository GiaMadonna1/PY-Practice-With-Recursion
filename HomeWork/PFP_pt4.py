def max_num(val1, val2, val3):
    return max(val1, val2, val3)

# print(max_num(val1=10, val2=20, val3= 5))

def mult_list(lst):
    if len(lst) == 0:
        return 0
    
    prod = lst[0]

    if len(lst) > 1:
        for i in lst[1:]:
            prod = prod * i

        return prod

# print(mult_list([5, 6, 4]))

def rev_string(string):
    return string[::-1]

# print(rev_string("Don't Work At Chili's"))

def num_within(u, a, b):
    return u in range(a, b+1)
    
# print(num_within(1,6,7))

triangle = [[1], [1,1]]
def pascal(n):
    if n < 1:
        print("invalid number")
    elif n == 1:
        print(triangle[0])
    else:
        row_number= 2

        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]

            length = len(row_prev)+1
            for i in range(length):

                if i == 0:
                    row.append(1)

                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1][i-1]+triangle[row_number - 1][i])

                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

            for row in triangle:
                print(row)

print(pascal(8))
