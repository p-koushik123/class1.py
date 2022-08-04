class parent:
    def function1(self):
        print("this is function one")
class Child(parent):
    def function2(self,a):
        print("tis function is two")
        print(a)
    b=20

y= Child()
y.function1()
y.function2(10)
print(y.b)