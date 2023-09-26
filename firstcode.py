def calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive):
    list = []
    for i in range(max_exclusive):
        if i%2==0 and i>0:
            list.append(i)
    list2 = []
    for i in range(max_exclusive):
        if i%7==0 and i>0:
            list2.append(i)
    def suma(list,list2):
        sum =0 
        sum2 = 0
        suma = 0
        for i in list:
            sum = sum + i
        for j in list2 :
            sum2 = sum2 + j
        suma = sum + sum2 
        return suma
    sumaa = suma(list,list2)
    print(f"Los numeros multiplos de dos: {list}")     
    print(f"Los numeros multiplos de 7 son: {list2}")
    print(f"El cardinal es: {len(list)+len(list2)}")
    print(f"La suma es: {sumaa}")
if __name__ == '__main__':
    calc_sum_and_count_all_numbers_div_by_2_or_7(8)