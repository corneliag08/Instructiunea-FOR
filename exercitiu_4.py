a=int(input("Dati numarul a:"))
s=0
for i in range(1,a):    
    if ((i%5==0)or(i%3==0)):
        s+=1
print("Suma numerelor ce se impart la 3 si 5 este:",s)