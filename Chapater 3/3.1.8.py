#Analyzing code of samples

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if num1 > num2:
    print(num1)

elif num2 > num1:
    print(num2)


#Next

rad1 = int(input('Enter a vallue: '))
rad2 = int(input('Enter a value: '))

if rad1 > rad2: print(f'Radius is {rad1}')
elif rad2 > rad1: print(f'Radius is {rad2}')


#Example 3

marks1 = int(input('Enter a value:'))
marks2 = int(input('Enter a Value: '))
marks3 = int(input('Enter a Value'))

if marks1>marks2>marks3:
    print (f'Marks1 is greater that is: {marks1}')
elif marks2 > marks1>marks3:
    print (f'Marks2 is greater that is: {marks2}')
else:
    print (f'Marks3 is greater that is: {marks3}')


