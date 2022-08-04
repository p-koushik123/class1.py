class medicine:
    a="null"
    def  __init__(self,a):
        self.a=a
    def show(self):
        print("no of medicines: ",self.a)
class doctor(medicine):
    b="null"
    c ="null"
    def __init__(self,a,b,c):
        super().__init__(a)
        self.b=b
        self.c=c
    def disp(self):
        print("name ",b)
        print("specification ",c)
class patient(doctor):
    d="null"
    e="null"
    def __init__(self,a,b,c,d,e):
        super().__init__(a,b,c)
        self.d=d
        self.e=e
    def dipsplay(self):
        print("enter id ",d)
        print("enter name ",e)
e=input("enter name ")
d=input("enter your id ")
c=input("enter doctor name ")
b=input("enter doctor specification ")
a=input("no of meds ")
obj=patient(a,d,c,d,e)
obj.dipsplay()
obj.disp()
obj.show()