while True:
    try:
        n=int(input("please enter an integer: "))
        break
    except IOError:
        print("Not an integer! please again 123")
    except ValueError:
        print("Not an integer! please again 456")

print("you successfully entered an integer!")
