num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
oper = input ('Enter operation (+, -, *, /): ')

if oper == '+':
  print(f'{num1} + {num2} = {num1 + num2 }')
elif oper == '-':
  print(f'{num1} - {num2} = {num1 - num2}')
elif oper == '*':
  print(f'{num1} * {num2} = {num1 * num2}')
elif oper == '/':
  print(f'{num1} / {num2} = {num1 / num2}' )
else: 
  print('Invalid Input')
