k = int(input())
a = []
b = []
for _ in range(k):
    Nazvanie = input('Введите название банка')
    Dengi = int(input('Кол-во денег'))
    Sbornik = (Nazvanie, Dengi)
    b.append(Sbornik)
    a.append(Dengi)

#Banki = ''
# indexovka = ''
if a[0] > a[1]:
    a[1] = a[0]
    # indexovka=0
    #  Banki = Banki+str(b[indexovka])
for i in range(2, k):
    if a[i] + a[i-2]>a[i-1]:
        a[i] = a[i]+a[i-2]
        # Banki.replace(b[indexovka],'')
        # indexovka = i
        # Banki = Banki + str(b[indexovka])

    else:
        a[i] = a[i-1]
        # Banki = Banki[:-1]
        # Banki = Banki + str(b[indexovka])
print(b, max(a))