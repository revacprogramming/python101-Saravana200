dict={}
with open("mbox-short.txt","r") as f:
    for l in f:
        if(l.startswith("From ")):
           dict[l.split()[1]]=dict.get(l.split()[1],0)+1
largest=0
di=None
for l in dict:
    if (dict[l]>largest):
        di=l
        largest=dict[l]
print(di,largest,sep=' ')