def extraer_digitos(num):
    while(num>0):
        digito = num%10
        num = num//10
        print(digito, end= ' ')
    print()
if __name__ == '__main__':       
    extraer_digitos(123)