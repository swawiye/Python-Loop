print("Number Meter")
print("Enter five numbers of your choice and it'll find the largest number and the smallest number!")

# Get five numbers from the user using input
numbers = []

for inp in range(5):
    num = int(input(f"Enter a number of your choice {inp + 1}: ")) # "{inp + 1}" increments the value by 1 for the range of five numbers
    numbers.append(num) # stores the values for later use, "print(num)" only displays the values

# Initializing the minimum and maximum values 
min_value = numbers[0]
max_value = numbers[0]

# Finding the smallest and largest numbers
for num in numbers:
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num

print("Smallest number:", min_value)
print("Largest number:", max_value)