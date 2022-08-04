class c:
    def disp(self):
       print("your ticket is booked")
class Reservation(c):
    __source="null"
    __destination="null"
    __name = "null"
    __nofp = "null"
    def __init__(self , source, destination, name,nofp):
            self.__source = source
            self.__destination = destination
            self.__name = name
            self.__nofp = nofp

    def display(self):
         print("enter the source :", self.__source)
         print("enter the destination:", self.__destination)
         print("enter the name :", self.__name)
         print("enter the nofp:", self.__nofp)



n1 = input("enter your source: ")
n2 =input("enter your destination: ")
n3 =input("enter your name: ")
n4 =input("enter your nofp: ")
obj =Reservation(n1,n2,n3,n4)
obj.display()
obj.disp()







