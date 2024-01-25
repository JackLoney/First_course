def analyze_lists(list1, list2):
    a=[]
    b=[]
    for i in list1:
        a.append(i)
    for j in list2:
        b.append(j)
    common = []
    extra = []
    for i in a:
        for j in b:
            if i == j:
                common.append(i)
                break
    for i in a:
        if i not in b:
            extra.append(i)

    for j in b:    
        if j not in a:
            extra.append(j)
            
    for i in common:
        a.remove(i)
        b.remove(i)      
    return common, extra, a, b

def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    
    result = analyze_lists(list1, list2)
    print(result) 
if __name__ == "__main__":
    main()
