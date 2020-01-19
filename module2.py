f=open('Perepis.txt','r')
l=list()
s=str()
s1=str()
a=int()
n=int(input("укажите menshee znachenie"))
b=int(input("укажите bolshee znachenie"))
for line in f:
    s=line
    s1=s[-5:-1:]
    if n<int(s1)<b:
        print(line)
        a+=1
print (a)

