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


