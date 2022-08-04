
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
print( "select operation.")
print("1.Add")
print("2.Subtract")
while True:
    choice = input("Enter choice(1/2):")

if choice in ('1', '2'):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second  number: "))
    if choice == 1:
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == 2:
        print(num1, "-", num2, "=", subtract(num1, num2))

     #ext calculation = input()

