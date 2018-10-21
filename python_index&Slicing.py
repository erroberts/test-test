print(5**2)
#25
print(9 * 5)
#45
print(15 / 12)
#1.25
print(12 / 15)
#0.8
print(15 // 12)
#1
print(12 // 15)
#0
print(5 % 2)
#1
print(9 % 5)
#4
print(15 % 12)
#3
print(12 % 15)
#12
print(6 % 6)
#0
print(0 % 7)
#0

#a. What does the “**” do? What’s its’ name in python?
# "**" is to exponent and is named Exponetiation

#b. What does the “*” do? What’s its’ name in python?
# "*" is to multiple and is named Multiplication

#c. What does the “/” do? What’s its’ name in python?
#"/" is for divide and is named Division

#d. What does the “//” do? What’s its’ name in python?
#"//" is for Floor divison which rounds basic division down and is named Floor Division

#e. What does the “%” do? What’s its’ name in python?
#"%" is for absolute vaule and is named Modulus

#2. Take the sentence: “All work and no play makes Jack a dull boy.”

a = 'All '
w = 'work '
an = 'and '
n = 'no '
p = 'play '
m = 'makes '
j = 'Jack '
o = 'a '
d = 'dull '
b = 'boy. '

print( a + w + an + n + p + m + j + o + d + b )


#Order of operations 3. Add parenthesis to the expression 6 * 1 - 2 to change its value from 4 to -6.

print(6*(1-2))


#Example for questions 4 - 7: Ex. Write a program that will convert user input minutes to hours:minutes.
#minutes = int(input("Enter number of minutes to convert to hours:minutes: "))
#hours = (minutes // 60)
#remainder = (minutes % 60)
#print("{0} Minutes converts to {1} Hour(s) & {2} Minute(s)".format(minutes,hours,remainder))

#4 Write a program that will compute the area of a rectangle.
# Prompt the user to enter the width and height of the rectangle.
# Print a nice message with the answer.

width = int(input("Width of Rectangle: "))
length = int(input("Length of Rectangle: "))
area = int(width * length)

print( "With great pleasure I present you the area of your Rectangle: ",area)

#5. Write a program that will compute the area of a circle.
# Prompt the user to enter the radius and print a nice message back to the user with the answer.
import math
math.pi
pi = float(math.pi)
R = int( input( "Enter radius:"))
area = int(pi *(R ** 2))

print( "With great pleasure I present you the area of your Circle: ",area)
#6. Take input from user. Write a program that will convert degrees celsius to degrees fahrenheit.

d = int(input("degrees as Celsius:" ))

f = int( (d* (5/9))+ 32)

print( "With great pleasure I present you Fahrenheit: ",f)

#7. Take input from user. Write a program that will convert degrees fahrenheit to degrees celsius.

g = int(input("degrees as fahrenheit:" ))

c = int( (g - 32)* (5/9))

print( "With great pleasure I present you Celsius ",c)


#0. Ex. Return the letter r from the string ‘Hello World’. greeting = ‘Hello World’ print(greeting[8]) >>>r Store the strings in an arbitrary variable of your liking.
#1. Return the letter p from the string 'Computer'.
com = 'Computer'
print(com[3])

#2. Return the letter b from the string 'Book'.
b = 'Book'
print(b[0])

#3. Return the letter s from the string 'Mouse'.
m = 'Mouse'
print(m[3])

#4. Return the letter z from the string 'This is a really long z'.
q = 'This is a really long z'
print(q[22])

#5. Return the word cat from the string 'concatenate'.
con = 'concatenate'
print(con[3:6])

#6. Return the word smith from the string 'blacksmith'.
bl = 'blacksmith'
print(bl[5:10])


#7. Return the word sign from the string 'designer'.
de = 'designer'
print(de[2:6])

#8. Return the word reframe from the string 'wireframe'.
wf = 'wireframe'
print(wf[2:10])

#9. Return the word k-E from the string 'Back-End'.
be = 'Back-End'
print(be[3:6])

#10. Return the word Java from the string 'JavaScript'.
j = 'Javascript'
print(j[0:4])

#11. Store your name in a variable called ‘name’. Write a string index that returns your name written backwards.
name = 'Ernest Roberts'
print(name[::-1])
