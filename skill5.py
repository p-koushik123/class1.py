class Confromation:
    def disp(self):
        print("your ticket ids booked!!")
class Details(Confromation):
    name=input("enter your name: ")
    no_of_p=input("enter No of passangers: ")
    type=input("enter Ac or Sleeper: ")
    def display(self):
        print("Name: ",self.name)
        print("No of passengers ",self.no_of_p)
        print("Type ",self.type)
class j(Details):
   source = input("enter your source: ")
   dest=input("enter your Destination: ")
   def show(self):
       print("source ",self.source)
       print("Destination: ",self.dest)
obj = j()
obj.disp()
obj.display()
obj.show()

