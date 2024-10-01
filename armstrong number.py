def generate_armstrong_numbers(up_to):
    armstrong_numbers = []
    for num in range(1, up_to + 1):
        num_str = str(num)
        num_digits = len(num_str)
        sum_of_digits = 0
        for digit in num_str:
            sum_of_digits += int(digit) ** num_digits
        if sum_of_digits == num:
            armstrong_numbers.append(num)
    return armstrong_numbers

armstrong_numbers = generate_armstrong_numbers(1000)
print("Armstrong numbers up to 1000:", armstrong_numbers)