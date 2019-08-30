# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output "Fizz" instead of the number
# and for multiples of five output "Buzz".  For numbers which are multiples
# of both three and five output "FizzBuzz".

# Expected Output:
# [
#   "1",
#   "2",
#   "Fizz",
#   "4",
#   "Buzz",
#   "Fizz",
#   "7",
#   "8",
#   "Fizz",
#   "Buzz",
#   "11",
#   "Fizz",
#   "13",
#   "14",
#   "FizzBuzz"
# ]

# Get the "n" value from the user
while True:
    try:
        up_to = int(input("Please enter a number to run up to: "))
    except ValueError:
        print("You did not enter a number!")
        continue
    else:
        break

def fizzbuzz(up_to_number):
    for number in range(1,up_to_number):
        if number == 0:
            print(number)
        elif number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
    return
    
fizzbuzz(up_to)

