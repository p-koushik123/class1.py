try:
    a= int(input("Enter a:"))
    b = int(input("Enter b:"))
    c=a/b
    print("a/b = %d"%c)

    #using exception object with the except statement
#except
except Exception as e:
    print("can't divide by zero")
    print(e)
else:
    print("Printing from else block")
