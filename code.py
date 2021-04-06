print ('Введите выражение:')
a = str(input())

summa = 0
raznitsa = 0

def suMma():
    a = a.split("+")
    summa = int()
    s = len(a)
    for x in range(0,len(a)):
        summa = int(summa + int(a[x]))

def raZnitsa():
    a = a.split("-")
    raznitsa = int()
    s = len(a)
    for x in range(0,len(a)):
        raznitsa = int(raznitsa + int(a[x]))

virazhenie = summa + raznitsa
#print(virazhenie)
print(summa)
print(raznitsa)
