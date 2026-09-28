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
n=int(input(":"))
while i<n :
    i+=1
    sum+=i
print(sum)
