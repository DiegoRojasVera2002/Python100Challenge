def primo(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True
list = []
for j in range(2,25):
    if primo(j):
        list.append(j)
print(list)
if __name__ == '__main__':
    pass