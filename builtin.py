#1
l=list(map(int,input().split()))
print(eval('*'.join(map(str,l))))

#2
s=input()
l=list(filter(lambda x: x.isupper(),s))
u=list(filter(lambda x: x.islower(),s))
print(f"lowercase: {len(l)}, uppercase: {len(u)}")

#3
a=input()
x=slice(0,len(a), 1)
c=slice(len(a),0,-1)
d=slice(1)
print(a[c]+a[d]==a)

#4
import time
a=float(input("Sample input:\n"))
t=float(input())
time.sleep(t/1000)
print(f'Sample output:\nSquare root of {a} after {t} milliseconds is {a**0.5}')

#5
t1 = (True, True, True, True)
t2 = (True, True, False, True)
t3 = (True, True, True, True)
t4 = (True, True, False, True)
print(all(t1),all(t2),all(t3),all(t4))