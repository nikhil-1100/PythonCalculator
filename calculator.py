# Program make a simple calculator

# This function adds two numbers
def add(x, y):
	return x + y

# This function subtracts two numbers
def subtract(x, y):
	return x - y

# This function multiplies two numbers
def multiply(x, y):
	return x * y

# This function divides two numbers
def divide(x, y):
	return x / y


menu = """
Select operation
1.Add
2.Subtract
3.Multiply
4.Divide
"""
print(menu)

while True:
	# Take input from the user
	choice = input("Enter choice(1/2/3/4): ")
	options = ('1', '2', '3', '4')
	# Check if choice is one of the four options
	if choice in options:
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))

		if choice == '1':
			print(f"{num1} + {num2} = {add(num1, num2)}")

		elif choice == '2':
			print(f"{num1} - {num2} = {subtract(num1, num2)}")

		elif choice == '3':
			print(f"{num1} * {num2} = {multiply(num1, num2)}")

		elif choice == '4':
			print(f"{num1} / {num2} = {divide(num1, num2)}")
		break
	else:
		print("Invalid Input !")
