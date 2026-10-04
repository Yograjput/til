'''Print all numbers from 1 to 10 using a loop.'''
i=0
while i < 10:
    i += 1
    print(i)


'''Print all numbers from 0 to 9 using a loop.'''
i = 0
while i < 10:
    print(i)
    i += 1


'''Print Numbers from 10 down to 1 in reverse order.'''
i=10
while i > 0:
    print(i)
    i -= 1

'''Print All Even Numbers between 1 to 100.'''
i=0
while i<100:
    i+=2
    print(i)

'''Print All odd numbers between 1 and 100.'''
i=1
while i<100:
    print(i)
    i+=2
    
'''Print the multiplication table of a given number from n*1 to n*10.'''
i=1
n=int(input("Enter the number:"))
while i <= 10:
    c=n*i
    print(c)
    i+=1


'''Calculate and print the sum of first n natural numbers.'''
i=0
sum=0
n=int(input("Enter the number:"))
while i<n :
    i+=1
    sum+=i
print(sum)


'''Calculate and print the sum of all even numbers from 1 up to n.'''
n = int(input("Enter the number: "))

i = 1
total = 0

while i <= n:
    if i % 2 == 0:
        total += i
    i += 1

print("Sum of even numbers:", total)



'''Calculate and print the sum of all odd numbers from 1 up to n.'''
n = int(input("Enter n: "))

i = 1
total = 0

while i <= n:
    if i % 2 != 0:
        total += i
    else:
        total += 0

    i += 1

print("Sum of odd numbers:", total)

'''Calculate and print the factorial of the given number.'''
n = int(input("Enter n: "))

i = 1
c=1

while i <= n:
    c=c*i
    i += 1

print(c)


'''Find and print the product of all digits of a given number.'''
n = int(input("Enter a number:"))
i=1
c=1

while n>0 :
    i=n%10
    c=c*i
    n=n//10


print("Product of all digits of a number:",c)


'''Count and print the total number of digits in a given number.'''
n = int(input("Enter a number:"))
i=0
c=0

while n>0 :
    i=n%10
    c=c+1
    n=n//10


print("Total number of all digits of a number:",c)

'''Find and print the sum of all digits of a number.'''
n = int(input("Enter a number:"))
i=0
c=0

while n>0 :
    i=n%10
    c=c+i
    n=n//10


print("Sum of all the digits of entered number:",c)

'''Reverse the given number and print the reversed value.'''
n=int(input("Enter a number: "))


is_negative= False
if n<0:
  is_negative= True
  n=-n
  
c=0




while n>0:
  i=n%10
  c=c*10+i
  n=n//10

if is_negative==True: 
  c=-c



print(c)

'''Check whether a given number is a palindrome or not.'''
n=int(input("Enter a number: "))
d=n  
c=0


while n>0:
  i=n%10
  c=c*10+i
  n=n//10


if d==c:
  print("We've got a palindrome!")
else:
  print("No Palindromes!")

'''Check whether the entered number is a palindrome or not.'''
n=input("Enter a number: ")
m=len(n)
i=1
c=0
b=int(n)


while b>0:
  i=b%10
  c=c+(i)**m
  b=b//10


if c==int(n):
  print("This is a Armstrong number.")
else:
  print("This is Not a armstrong number.")



'''Check whether the entered number is a Perfect Number.'''
n=int(input("Enter the number:"))

i=1
c=0
p=n*2

while i<=n:
  if n%i==0:
    c=c+i
    i=i+1
    
  else:
    i=i+1


if c==p:
  print("Perfect Number")
else:
  print("Not a perfect Number")

'''Print all the prime numbers from 1 to 100.'''
n=1
while n<=100:
  fac=0
  i=1
  while i<=n:
    if n%i==0:
      fac=fac+1
      i=i+1
    else:
      i=i+1

  if fac==2:
    print(n)

  n=n+1


'''Check whether the entered number is prime number or not.'''
n=int(input("Enter a number:"))

fac=0
i=1
while i<=n:
  if n%i==0:
    fac=fac+1
    i=i+1
  else:
    i=i+1


if fac==2:
  print("This is a prime number")
else:
  print("This is not a prime number.")
  
'''Print the Fibonacci Series upto n terms.'''
n=int(input("Enter a number:"))
i=0

a=0
b=1
c=1
while i<n:
  print(a)
  c=a+b
  a=b
  b=c
  i=i+1


'''Print the sum of Fibonacci series upto n terms.'''
n = int(input("Enter a number: "))
i = 0
a = 0
b = 1
c = 0
r = 0  

while i < n:
    c = a + b
    r = r + c  
    a = b
    b = c
    i = i + 1

print("The final sum is:", r)

'''Print the squares of numbers from 1 to n.'''
n=int(input("Enter a number:"))
i=0
c=1
while i<n:
  i=i+1
  c=i**2
  print(c)

'''Print the cube of numbers from 1 to n.'''
n=int(input("Enter a number:"))
i=0
c=1
while i<n:
  i=i+1
  c=i**3
  print(c)

'''Print the numbers between a and b that are divisible by 7.'''
a=int(input("Enter a number:"))
b=int(input("Enter a number greater than first number:"))
i=a
c=0
while i<=b:
  if i%7==0:
    print(i)
    i=i+1
  else:
    i=i+1


