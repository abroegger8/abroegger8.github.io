#anything that begins with a # is a comment and comments are code that doesn't get executed

print('hello world')
print('goodbye world')

var1 = 'hello'
var2 = 'world'
var3 = var1 + ' ' + var2 
print(var3)

''' this is a triple quote
everything inside this will be ignored
'''

# for integers, python is always going to give you exact results;
x = 1 
y = 5 
z = x + y 
print(z)

# non-integer number; (fractions, irrational numbers) are approximations
# the type of a number with a period is called a float
x = 0.1
y = 0.1
z = 0.1
q = x + y + z 
print (q)

# the last type is the str = "string" type, for strings

#python is an "untyped language" because we can change the type at anytime 

x = 'this is a string'
print(x)

# import is a keyword; math=package/library that we are importing
import math

# psuedocode for the quadratic formula: 
# (a**2 +- sqrt(b-4ac))/2a
a = 5 
b = 100
c = 2
quadratic1 = (a**2 + math.sqrt(b - 4 * a * c)) / (2 * a)
print(quadratic1)
quadratic2 = (a**2 - math.sqrt(b - 4 * a * c)) / (2 * a)
print(quadratic2)

a = 3 
quadratic1 = (a**2 + math.sqrt(b - 4 * a * c)) / (2 * a)
print(quadratic1)
print(quadratic2)
# python does not update variables (only first quadratic is printed above compared to both of them)

# functions and variables are the key differences between Python on HTML/CSS
def quadritic(a, b, c):
    result = (a**2 - math.sqrt (b-4 * a * c)) / (2 * a)
    return result
    
    print (quadratic(5, 100, 2)
    print (quadritic(3, 100, 2))

x = 5
y = 29 
print (x // y)
print (y % x) #percent is the "modulus operator"; which is the remainder

#if you want to check that two things are equal to each other you must use the double equals sign ==

print(math.pi)

'''
quadratic_formula # this is called snake case
quadraticFormula # this is called camel case
'''
#python uses snake case!!!