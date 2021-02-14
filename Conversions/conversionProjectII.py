'''
Created on Feb 14, 2021

@author: Anna R

The Objective is to make a program that can complete different conversions. The tasks to complete are:
 convert yards to miles, miles to feet, miles to inches. 

'''
#Use input() to get the number of miles from the user. And store
#that int in a variable called miles.
mile = 1
#Convert miles to yards, using the following:
# 1 mile = 1760 yards.

#Store the value in a variable called yards and print it out with a 
#simple statement.
yards = mile * 1760
print (str(mile) + " mile converts to " + str(yards) + " yards ")

#Convert miles to feet, using the following:
# 1 mile = 5280 feet.
feet = 5280
#Store the value in a variable called feet and print it out with a 
#simple statement.
feet = mile * 5280
print (str(mile) + " mile converts to " + str(feet) + " feet ")
#Convert miles to inches, using the following:
# 1 mile = 63,360 inches.

#Store the value in a variable called inches and print it out with a 
#simple statement.
inches = mile * 63360 
print (str(mile) + " mile converts to " + str(inches) + " inches ")