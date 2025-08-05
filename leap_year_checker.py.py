# Leap Year Checker

# Ask the user to input a year
year = int(input("Enter a year: "))

# Check if the year is a leap year
# Rule:
#  - Divisible by 4, AND
#     - Not divisible by 100 UNLESS divisible by 400
leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Output result
if leap:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

number = int(input("enter number: "))
odd_even= number/2
if odd_even == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
