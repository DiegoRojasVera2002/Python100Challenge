def conteo_digito(num):
    cont = 0
    while(num>0):
        num = num//10
        cont+=1
    print(cont,end='')
if __name__ == '__main__':
    conteo_digito(123)