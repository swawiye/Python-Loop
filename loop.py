numbers = [24, 13, 57, 689, 9, 68, 72, 454, 32, 5, 6, 897, 8, 96, 54, 37, 26, 43, 25, 7, 68, 989, 6, 54, 73, 26, 243, 5, 76, 8]

# Initializing the variables to the first element of the list of numbers
min_value = numbers[0]
max_value = numbers[0]

for number in numbers:
    if number < min_value:
        min_value = number
    if number > max_value:
        max_value = number

print("Smallest number:", min_value)
print("Largest number:", max_value)
