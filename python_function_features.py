#Takes in any number of arguments and prints them one at a time.

def arb_args(*args):
    for i in args:
        print(i)

arb_args("this is a string", "name", 1, True)


#Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. 
# The result of both nested functions should then be added together and printed.

def inner_func(a, b):
    def inner1():
        return a + b
    def inner2():
        return b - a
    print(inner1() + inner2())

inner_func(10, 15)

#Takes in two strings: a student's name and their lunch preference. The function should print both strings.
#If a lunch preference is not given, "Mystery Meat" should be printed instead.

def lunch_lady(name, lunch="mystery meat"):
    print(name + ' ' + lunch)

lunch_lady("Chandler", "tacos")
lunch_lady("Chandler2")


#Accepts two integers and returns both the sum and the product.

def sum_n_product(a, b):
    sum = a + b
    product = a * b
    return(sum, product)

print(sum_n_product(10, 3))

#Solution

def sol_sum_n_product(a, b):
    return(a+b,a*b)


print(sol_sum_n_product(5, 3))

#Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. 
#Alternatively, you can call a function from inside another function.

alias_arb_args = arb_args

#Accepts any number of integers and prints their average.

def arb_mean(*args):
    total = 0
    for i in args:
        total += i
    print(total/len(args))

arb_mean(4, 5, 6)

#Accepts any number of strings and returns the longest one.

def arb_longest_string(*args):
    longest = 0
    string = ''
    for i in args:
        string_length = len(i)
        if string_length > longest:
            string = i
        #else: works with and without else 
            string = string
    print(string)

arb_longest_string("short", "longer", "no", "this is the longest")