list_of_strings = input().split(',')
number = [int(num) for num in list_of_strings]
result = [num for num in number if num % 2 == 0]
print(result)