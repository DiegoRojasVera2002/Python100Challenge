def divisores(num):
    list = []
    cont = 1
    while(cont<=num):
        if num%cont==0:
            list.append(cont)
        cont+=1
    return list
if __name__ == '__main__':
    print(divisores(12))