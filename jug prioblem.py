x=int(input("please enter the value x:"))
y=int(input("please the value of y:"))
while True:
    case=int(input("Enter the case no"))
    if case==1:
        if x<4:
             x=4
    if case==2:
        if y<3:
              y=3
    if case==5:
        if x>0:
              x=0
    if case==6:
        if y>0:
              y=0
    if case==7:
        if  x+y>=4 and y>0:
            x,y=4,y-(4-x)
    if case==8:
        if x+y>=3 and x>0:
             x,y = x-(3-y),3
    if case==9:
        if x+y<=4 and y>0:
             x, y = x+y,0
    if case==10:
        if x+y<=3 and x>0:
            x, y = 0,x+y
    print("x =",x)
    print("y =",y)
    if(x==2):
          print("the result is a final state")
          break