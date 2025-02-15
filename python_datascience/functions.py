def square(a_number):
    return a_number ** 2

def double(x):
    return x * 2

#function with arguments

def full_name(first_name, last_name):
    return first_name + " " + last_name

#function with default arguments
def greet(name = "World"):
    return "Hello " + name + "!"
#function with variable arguments
def sum_values(*args):
    return sum(args)

def sum_all(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

print(sum_all(1, 2, 3)) # Prints 6

