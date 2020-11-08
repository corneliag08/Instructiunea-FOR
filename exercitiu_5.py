a1=int(input("Introdu a1 :"))
a2=int(input("Introdu a2 :"))
a3=int(input("Introdu a3 :"))
a4=int(input("Introdu a4 :"))
a5=int(input("Introdu a5 :"))
a6=int(input("Introdu a6 :"))
s1=0
s2=0
s3=0
s4=0
s5=0
s6=3
for i in range(1,a1+1):
    s1+=i
for i in range(2,a2+1):
    s2+=(i-1)*i
for i in range(1,a3+1):
    p=1
    for a in range(1,i+1):
        p*=a
    s3+=p
for i in range(1,a4+1):
    s4+=i*10+2
for i in range(1,a5+1):
    s5+=i/(i+1)
for i in range(2,a6+1):
    if i<10:
        s6+=20+i
    else:
        s6+=20*(10**(i//10))+i
print("s1=",s1)
print("s2=",s2)
print("s3=",s3)
print("s4=",s4)
print("s5=",s5)
print("s6=",s6)
