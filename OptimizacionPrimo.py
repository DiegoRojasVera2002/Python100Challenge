def primos(num):
    list = []
    for i in range(2,num+1):
        valor = True
        for j in range(2,i):
            if i%j==0:
                valor = False
                break
        if valor:
            list.append(i)
            print(i,",",end="")
if __name__ == '__main__':
    primos(25)