'''
This outline will help solidify concepts from the Logical Operators lesson.
Fill in this outline as the instructor goes through the lesson.
'''

'''The green words in the problems are for me to look back through, it's the notes i took 
on the logical operator video'''
#EX) Make two boolean variables. Put them on either side of the and operator.
#Store this expression in a variable named a. Print the variable.
one = True
two = False
a = one and two 
print(a)

#1) Make two boolean variables. Put them on either side of the and operator.
#Store this expression in a variable named a. Print the variable.
w = 4
z = 5
a = w==w and z==z
print(a)

h=4
g=5
a= h==h and g==g
print (a)
#true      #true
'''4 == 4 and 5 == 5'''
#true


# more examples 
#false     #true
'''2 == 4 and 5 == 5
#false

username = "anna"
password = "rusch"

boolean = (username == "anna") and (password == "rusch")
print (boolean)'''
#2) Make two boolean variables. Put them on either side of the or operator.
#Store this expression in a variable named b. Print the variable.
#false    #true
'''2 == 4 or 2 == 5'''
#true
d = 2
j = 2
p = 4 
x = 5
b = d==p or j==x
print (b)

t=2
h=5
u=3
b= t==t or h==u
print (b)
#more examples
''''2 < 3 or 5 < 10
#true

4 < 3 or 5 < 10
#true

4 < 3 or 3 < 2
#false'''
#3) Make one boolean variable. Put the variable after the not. Store this 
#expression in a variable named c. Print the variable.
g=3
c= not g==g
print (c)
 
'''
not 3==3
#false

not 4==5
#true'''
#4) Make a logical expression with one of the common SYNTAX errors.

not 

3==3 5==6
'''
logical error could be:
username = "anna"
password = "rusch"

boolean = (username == "anna") OR (password == "rusch")
print (boolean)

but it should be AND so it's less easier for someone to hack into your accounts.
'''
