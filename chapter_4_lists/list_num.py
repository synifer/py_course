import numbers


numbers = list(range(1,6))
print(numbers)


even_num = list(range(2,11,2))
print(even_num)

# squares.py

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)