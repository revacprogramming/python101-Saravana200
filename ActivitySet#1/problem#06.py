largest,smallest=0,0
while True:
    try:
        num = input("Enter a number: ")
        if(num=='done'):
            break
        num=int(num)
    except:
        print("Invalid input")
        continue
    if(num>largest):
        largest=num
    elif(num<smallest or smallest==0):
        smallest=num
print("Maximum is", largest)
print("Minimum is", smallest)