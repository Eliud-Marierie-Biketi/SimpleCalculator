
#ELIUD MARIERIE      SCT211-0094/2022

name = input("Enter your name : ")

print(f"Welcome {name}, This is a simple calculator !\n")

first_number = input("Enter first number:")
second_number = input("Enter second number:")

addition =  float(first_number) + float(second_number)
subtraction = float(first_number) - float(second_number)
product = float(first_number) * float(second_number)
division = float(first_number) / float(second_number)


operation = input("Enter one of the operation for the two numbers above\nEither + (for addition),\t- (for subtraction),\t * for (multiplication)\t and / for (division):")
print("_________________________________________________________________")

if(operation == "+"):
    print(f"Sum of {first_number} and {second_number} is {addition}")
elif(operation == "-"):
    print(f"subtracting {first_number} from {second_number} gives {subtraction}")
elif(operation == "*"):
    print(f"Multiplication of {first_number} and {second_number} is {product}")
elif(operation == "/"):
    print(f"Division of {first_number} and {second_number} is {division}")
else:
    print("The operation Entered is invalid")
print("_________________________________________________________________")
