# Files

#filename = "dataset/mbox-short.txt"
# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
add,count=0,0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        num=""
        for t in line:
            if t.isdigit() or t==".":
                num=num+t
        add=add+float(num)
        count+=1
print("Average spam confidence:",add/count)