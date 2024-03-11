#Question 1:  Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
def calculate_discount(price, discount_percent):
    if discount_percent >=20:
        discounted_price = price - (price * discount_percent/100)
        return discounted_price
    else:
        return price
price = int(input('Enter the initial price of the item: '))
discount_percent = int(input('Enter the discount of the item displayed in Percentage: '))
print('The Final Price will be: ', calculate_discount(price, discount_percent))

# Question 2. Large Power
#Create a method that tests whether the result of taking the power of one number to another number provides an answer which is greater than 5000. We will use a conditional statement to return True if the result is greater than 5000 or return False if it is not. In order to accomplish this, we will need the following steps:
#Define the function to accept two input parameters called base and exponent
def large_power(base, exponent):
    # Calculate the result of base to the power of exponent
    result = base ** exponent
    
    # Use an if statement to test if the result is greater than 5000. f it is then return True. Otherwise, return False
    if result > 5000:
        return True
    else:
        return False

# Calling function with example inputs 
print(large_power(100, 3))  # Output: True
print(large_power(2, 10))  # Output: False
print(large_power(3, 3))   # Output: False

#Question 3: Create a function that determines whether or not a number is divisible by ten. A number is divisible by ten if the remainder of the number divided by 10 is 0. Using this, we can complete this function in a few steps:
#Define the function header to accept one input num
#Calculate the remainder of the input divided by 10 (use modulus)
#Use an if statement to check if the remainder was 0. If the remainder was 0, return True, otherwise, return False
def divisible_by_ten (num):
    if num%10 ==0:
        return True  #Use return when you want the function to compute a value and provide it to the caller for further processing
    else:
        return False
num = int(input('Enter a number: '))
print(divisible_by_ten(num))


# Question 4: Write a simple python program that can rate students performance as follows: score above 80=distinction, score between 60-70 = credit, score between 40-50 = fair and any other score below 40= fail.
score = int(input('Please Enter Your Subject Score: '))
if score >= 80:
    print('Congratulations! You have a distinction')
elif score >=60 and score<=70:
    print('You have Credit')
elif score >=40 and score<=50:
    print('You have Fair results')
else:
    print('Fail')


# Question 5: Create a simple calculator using python that can perform the following operations. Addition, Multiplication, Divisions, Subtraction.
    
def add(x, y):  #This line defines a function called add that takes two parameters x and y. Inside the function, it returns the result of adding x and y.
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y
 
#  This line defines a function called divide that takes two parameters x and y. Inside the function, it first checks if y is equal to zero. If it is, it returns the string "Cannot divide by zero!". Otherwise, it returns the result of dividing x by y.
def divide(x, y): 
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

#These lines print a menu to the console, prompting the user to select an operation.
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# This line starts an infinite loop that keeps running until it is explicitly broken. Inside the loop, it prompts the user to enter their choice of operation and stores it in the variable choice.
while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

# These lines check the user's choice and call the corresponding function (add, subtract, multiply, or divide) with the input numbers. It then prints the result.
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

# These lines prompt the user if they want to perform another calculation. If the user's input is not equal to "yes" (case insensitive), the loop breaks, ending the program. Otherwise, the loop continues, allowing the user to perform another calculation.
    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        break

#Question 6: performing calculations on multiple numbers rather than just two by modifying the functions to accept a variable number of arguments using the *args syntax. 
# This function add accepts a variable number of arguments (*args). It calculates the sum of all the numbers passed as arguments using the built-in sum() function and returns the result.
def add(*args):
    return sum(args)

# The subtract function also accepts a variable number of arguments (*args). It initializes the result variable with the first number in args, then iterates through the remaining numbers in args and subtracts them from result. Finally, it returns the result.
def subtract(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

# This function multiply accepts a variable number of arguments (*args). It initializes the result variable with 1 (since multiplying by 1 does not change the value) and then iterates through all the numbers in args, multiplying them with result. The final result is returned.
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

# The divide function accepts a variable number of arguments (*args). It initializes the result variable with the first number in args, then iterates through the remaining numbers in args. It checks if any of the numbers in args are zero (since division by zero is undefined), and if so, it returns the string "Cannot divide by zero!". Otherwise, it performs the division operation sequentially and returns the final result.
def divide(*args):
    result = args[0]
    for num in args[1:]:
        if num == 0:
            return "Cannot divide by zero!"
        result /= num
    return result

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        numbers = []  # Initialize an empty list to store the numbers. This list will store the numbers inputted by the user. It then prints a message instructing the user to enter the numbers for calculation, indicating that they should enter 'done' when they have finished.
    print("Enter the numbers for calculation (enter 'done' when finished):")

#This line starts a loop that will continue indefinitely until explicitly broken
    while True:
        num_input = input("Enter a number or 'done' to finish: ")
        
        if num_input.lower() == 'done':
            break  # Exit the loop if the user enters 'done'
        
#Inside the loop, the program attempts to convert the user's input (num_input) to a float using float(). If the conversion is successful (i.e., the input is a valid number), the number is added to the numbers list using the append() method. If the conversion fails (e.g., if the user enters a non-numeric input), a ValueError exception is raised, and the program prints an error message asking the user to enter a valid number or 'done'.
        try:
            num = float(num_input)  # Convert the input to a float
            numbers.append(num)  # Add the number to the list
        except ValueError:
            print("Invalid input! Please enter a valid number or 'done'.")

#After the loop exits (either because the user entered 'done' or due to an invalid input), the program checks if any numbers were entered by checking if the numbers list is empty. If no numbers were entered, it prints a message indicating that no numbers were entered and uses continue to skip the rest of the loop and prompt the user again.
    if not numbers:
        print("No numbers entered. Please try again.")
        continue  # Go back to the beginning of the loop to prompt the user again
        
    # Perform the calculation based on the user's choice and the input numbers
    if choice == '1':
        print("Result:", add(*numbers))
    elif choice == '2':
        print("Result:", subtract(*numbers))
    elif choice == '3':
        print("Result:", multiply(*numbers))
    elif choice == '4':
        print("Result:", divide(*numbers))


