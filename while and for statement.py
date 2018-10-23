#For loop - Easy
"""Create a for loop that will print all the numbers from 1-8, inclusive.
ex. for num in numbers
  print(num)"""
#code here
##numbers = ['1','2','3','4','5','6','7','8']
for num in range(9):
    print(num)

#For loop - Medium
"""Create for for loop that will print off all the even number from 1-100
Look up the range() function on Google. This will help."""
#code here
for black in range(0,101,2):
    print(black)


#For loop - Hard
"""
Write a program which uses a while loop to sum the squares of
intergers (starting from 1) until the total exceeds 200.

Print the final total and the last number to be squared and added.
ex. 1**2 = 2
    2**2 = 4
    3**2 = 9
    4**2 = 16
    2+4+9+16 = 31

    Write code to do this all the way up to 200.
"""
#code here
p = int()
sa = ''
n =0
for n in range(20):
    n += 1
    sa = n**2
    if sa <= 200:
        p += sa
        if p > 200:
            print ('the vaule went over 200 at:{0} with the value of:{1}'.format(n,p))
            break
    
    

        


    ##################################################################
#for loop - Easy
"""Using for Loops -  create a list of all numbers
between 1 and 50 that are divisible by 3."""
#code here
dn = []
for d in range(3,51,3):
    dn.append(d)
print(dn)
    
    
#for loop - Medium
"""Write a program that prints the integers from 1 to 100.
But for multiples of three print "Fizz" instead of the number, and
for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print 'FizzBuzz'."""
#code here

for v in range(0,101):
    if v % 5 == 0 and v % 3 == 0:
        print('fizzbuzz')
    elif v % 5 == 0:
        print('buzz')
    elif v % 3 == 0:
        print('Fizz')
    else:
        print(v)
        
