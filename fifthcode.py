def calc_primes_up_to(max_value):
    list2 = []
    for j in range(2,max_value+1):
        list = [i for i in range(1,j+1) if j % i == 0]
        if (len(list)==2):
            list2.append(j)
    return list2
if __name__ == '__main__':
    number = int(input("Ingrese un numero: "))
    print(calc_primes_up_to(number))    