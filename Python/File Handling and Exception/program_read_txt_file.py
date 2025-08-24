with open('input.txt', 'w') as file:
    file.write('This is a program')
    file.write('It contain code')
    file.write('It is python')
    file.write('I run it')
    file.write('it is a success')

with open('input.txt', 'r') as file:
    content = file.read()

#count the number of words in line
count_word = len(content.split())

#convert all text to uppercase
input_upper = content.upper()

with open('output.txt', 'w') as outfile:
    outfile.write(input_upper)
    outfile.write(str(count_word))

print('\n output.txt has been successfully created')
