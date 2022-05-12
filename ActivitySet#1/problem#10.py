count=0
with open("mbox-short.txt","r") as file:
    for i in file:
        if(i.split(' ')[0]=="From" and len(i.split())>2):
            print(i.split()[1])
            count+=1
print("There were", count, "lines in the file with From as the first word")
