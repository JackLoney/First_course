def main():
    k = int(input('Кол-во банков: '))
    a = []
    b = []
    for _ in range(k):
        Name_bank = input('Введите название банка: ')
        Money = int(input('Кол-во денег: '))
        Collection_Bank = (Nazvanie, Dengi)
        b.append(Sbornik)
        a.append(Dengi)
    
    #Bank = ''
    # index_b = ''
    if a[0] > a[1]:
        a[1] = a[0]
        # indexovka=0
        #  Bank = Bank+str(b[index_b])
    for i in range(2, k):
        if a[i] + a[i-2]>a[i-1]:
            a[i] = a[i]+a[i-2]
            # Bank.replace(b[index_b],'')
            # index_b = i
            # Bank = Bank + str(b[index_b])
    
        else:
            a[i] = a[i-1]
            # Bank = Bank[:-1]
            # Bank = Bank + str(b[index_b])
    print(b, max(a))
if __name__ == "__main__":
    main()
