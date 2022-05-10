def computepay(h, r):
    pay=h*r
    if (h>40):
        pay=40*r+(h-40)*1.5*r
    return pay
hrs=float(input("enter the hours: "))
rate=float(input("enter the rate: "))
print("Pay", computepay(hrs,rate))