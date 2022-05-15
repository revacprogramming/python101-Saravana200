a={}
with open("mbox-short.txt","r") as f:
    for i in f:
        if(i.startswith("From") and len(i.split())>3):
            t=(i.split()[5]).split(':')[0]
            a[t]=a.get(t,0)+1
l=list(a.items())
l.sort()
a=dict(l)
for i in a:
    print(i,a[i],sep=' ')