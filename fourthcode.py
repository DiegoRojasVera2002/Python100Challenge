def cal_perfect_numbers(max_exclusive):
    list2 = []
    for j in range(1,max_exclusive+1):
        list = [i for i in range(1,j) if j%i ==0 ]
        num = 0
        for i in list:
            num = num + i
        if (num == j):
            list2.append(j)
    return list2
if __name__ == '__main__':
    max_exclusive = int(input("Ingrese un numero: "))
    print(cal_perfect_numbers(max_exclusive))