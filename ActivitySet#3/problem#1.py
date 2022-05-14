n=int(input("enter the number of rectangles: "))
for i in range(0,n):
    x1,y1,x2,y2,x3,y3=input().split()
    print((((float(x2)-float(x1))**2+(float(y2)-float(y1))**2)**0.5)*((float(x3)-float(x2))**2+(float(y3)-float(y2))**2)**0.5)