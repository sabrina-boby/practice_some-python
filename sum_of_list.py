

def add_numbers(num):
    result = 0
    for number in num:
        result += number
    return result

result = add_numbers([1, 2, 30, 4, 5, 9])
print(result)