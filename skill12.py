class circle:
    rad="NULL"
    def cperi(self,r):
        cirperi=self.rad*2*3.14
        print("Perimeter of Circle :",cirperi)
class rectangle:
    len="NULL"
    bre="NULL"
    def rperi(self,l,b):
       recperi=2*(self.len+self.bre)
       print("Perimeter of Rectangle :",recperi)
class triangle:
    sid1="NULL"
    sid2="NULL"
    sid3="NULL"
    def tperi(self,s1,s2,s3):
        tperi=self.sid1+self.sid2+self.sid3
        print("Perimeter of Triangle :",tperi)
class perimeter(circle,rectangle,triangle):
    def init(self,r,l,b,s1,s2,s3):
        self.radius=r
        self.length=l
        self.breadth=b
        self.sid1=s1
        self.sid2=s2
        self.sid3=s3
p=perimeter(input(),input(),input(),input(),input(),input())
p.cperi(p.rad)
p.rperi(p.len,p.bre)
p.tperi(p.sid1,p.sid2,p.sid3)