l=[]
with open("romeo.txt","r") as file:
    for i in file:
        for word in i.split():
            if (word in l)==False:
                l.append(word)
l.sort()
print(l)