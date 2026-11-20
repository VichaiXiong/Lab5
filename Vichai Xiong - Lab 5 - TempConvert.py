#Have the program write a table of Fahrenheit and Celsius temperatures to a text file

with open('tempConv.txt', 'w') as temp_file:
    temp_file.write('Fahrenheit'.center(10))
    temp_file.write('Celsius'.center(10) + "\n")
    fahrenheit = range(-300, 213, 1)
    for temp in fahrenheit:
        cel = (5/9)*(temp-32)
        cel = (format(cel, '.2f'))
        temp = (format(temp, '.2f'))
        temp_file.write(temp.center(10))
        temp_file.write(cel.center(10) + '\n')