                #LIST COMPREHENSIONS

list = [1, 2, 3, 4]
total = sum(list)
print(total)

#pgm for printing  squares
squares = [x**2 for x in range (1, 6)]
print (squares)\


#pgm for printing even numbers
numbers = [1, 2, 3, 4, 5,  6, 7, 8, 9, 22, 44, 46, 78, 97, 55]

even_num = []
for num in numbers:
    if num % 2 == 0:
        even_num.append(num)
print(even_num)

even_num = [num for num in numbers if num % 2 == 0 ]
print(even_num)


#pgm for printing squares of even numbers
squares = [x**2 for x in range (1, 10) if x % 2 != 0]
print (squares)