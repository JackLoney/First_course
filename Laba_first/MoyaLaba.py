#Isheyka - Рекурсивная функия для поиска решения задачи
def Isheyka(colvo,ishem,poluchaem):
    global polka
    global kucha
    if polka != '':
        return 0
    if colvo == len(kucha):
        if ishem == S:
            polka = poluchaem
        return 0
    Isheyka(colvo + 1, ishem + int(kucha[colvo]), poluchaem+'+'+str(kucha[colvo]))
    Isheyka(colvo + 1, ishem - int(kucha[colvo]), poluchaem+'-'+str(kucha[colvo]))

#Присваиваем переменным значения из файла
with open('input.txt', "r") as file:
    Vse = file.readline().strip().split()
    N = int(Vse[0])
    S = int(Vse[-1])
    kucha = Vse[1:-1]

#Polka будет содержать искомую комбинацию    
polka = ''

#Необходимые условия выполнения
if N >= 2 and N <= 30 and S >= -10**9 and S <= 10**9:
    Isheyka(1,int(kucha[0]),str(kucha[0]))
    if polka == '':
        resultat = 'No solution'
    else:
        resultat = polka + '=' + str(S)
else:
    resultat = 'No solution'


#Запись руезльтата в файл
with open("output.txt", "w") as file:
        file.write(resultat)
