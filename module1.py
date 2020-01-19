f=open('Perepis.txt','r')
l=list()
s=str()
s1=str()
a=int()
for line in f:
    s=line
    s1=s[-5:-1:]
    if int(s1)<1978:
        print(line)
        a+=1
    print(a)


