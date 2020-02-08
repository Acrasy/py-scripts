import random
n=i=key1=key2=key3=0
num=""
print('hello world...aehm...na ... id  pls\nowa 10stellig')

while(len(num)!=10):
    num=input("die num lautet:\n")
#num=1910303018

if(num.isdigit()):
    seed=sum([int(value) for value in str(num)])

else:
    print("hawara... a nummer suist eingeben")
    quit()

while(key1%seed!=0 or not 99<key1<1000):
    n=random.randint(2,55) 
    key1=n*seed
while(key2==key1 or not 99<key2<1000 ):
    n=random.randint(2,55) 
    key2=n*seed
while(i%seed==0):
    i=random.randint(100,999)
    key3=i
print("your key is "+str(key1)+"-"+str(key2)+"-"+str(key3))
