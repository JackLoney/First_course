def analyze_lists(list1, list2):
    a=[]
    b=[]
    for i in list1:
        a.append(i)
    for j in list2:
        b.append(j)
    obshie = []
    lishnie = []
    for i in a:
        for j in b:
            if i == j:
                obshie.append(i)
                break
    for i in a:
        if i not in b:
            lishnie.append(i)

    for j in b:    
        if j not in a:
            lishnie.append(j)
    for i in obshie:
        a.remove(i)
        b.remove(i)      
    return obshie, lishnie, a, b
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

result = analyze_lists(list1, list2)
print(result) 
