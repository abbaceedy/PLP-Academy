#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
print('How many numbers do you want to enter? ')
count = int(input)

numbers = []
for i in range(count):
  num = int(input('Enter number: '))
  numbers.append(num)

print(numbers)
print(sum(numbers))
