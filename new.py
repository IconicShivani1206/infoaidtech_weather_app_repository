# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

# Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function to find the maximum of three numbers
def max_of_three(a, b, c):
    return max(a, b, c)

# Function to count the number of vowels in a string
def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

# Function to reverse a string
def reverse_string(string):
    return string[::-1]

# Function to write a list of numbers to a text file
def write_numbers_to_file(numbers, filename):
    with open(filename, "w") as file:
        for num in numbers:
            file.write(str(num) + "\n")

# Function to read numbers from a text file
def read_numbers_from_file(filename):
    numbers = []
    try:
        with open(filename, "r") as file:
            numbers = [int(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        return "File not found!"
    return numbers

# Function to sort a list of numbers
def sort_numbers(numbers):
    return sorted(numbers)

# Main function to demonstrate the functionalities
def main():
    # Math operations
    print("Addition of 3 and 5:", add(3, 5))
    print("Subtraction of 10 from 20:", subtract(20, 10))
    print("Multiplication of 4 and 6:", multiply(4, 6))
    print("Division of 10 by 2:", divide(10, 2))
    print("Division of 10 by 0:", divide(10, 0))

    # Checking even or odd
    num = 7
    print(f"{num} is", check_even_odd(num))

    # Finding the maximum of three numbers
    print("Maximum of 3, 5, and 2:", max_of_three(3, 5, 2))

    # String operations
    string = "Hello World"
    print("Vowel count in string 'Hello World':", count_vowels(string))
    print("Reversed string:", reverse_string(string))

    # File handling
    numbers = [1, 3, 5, 7, 9]
    filename = "numbers.txt"
    write_numbers_to_file(numbers, filename)
    print(f"Numbers written to {filename}")

    numbers_from_file = read_numbers_from_file(filename)
    print(f"Numbers read from file: {numbers_from_file}")

    # Sorting numbers
    sorted_numbers = sort_numbers(numbers)
    print("Sorted numbers:", sorted_numbers)

# Call main function
if __name__ == "__main__":
    main()
