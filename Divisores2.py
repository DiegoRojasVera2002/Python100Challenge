def Divisores(num):
    list = [i for i in range(1,num+1) if num%i==0 ]
    return list
if __name__ == '__main__':
    print(Divisores(24))