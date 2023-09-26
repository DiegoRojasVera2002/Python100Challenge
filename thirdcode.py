def ingrese_numero():
    n = int(input("Ingrese un numero: "))
    return n
def number_as_text(n):
    residuo = n % 10
    valor_a_texto = ""
    if residuo == 0:
        valor_a_texto = "CERO"
    if residuo == 1:
        valor_a_texto = "UNO"
    if residuo == 2:
        valor_a_texto = "DOS"
    if residuo == 3:
        valor_a_texto = "TRES"
    if residuo == 4:
        valor_a_texto = "CUATRO"
    if residuo == 5:
        valor_a_texto = "CINCO"
    if residuo == 6:
        valor_a_texto = "SEIS"
    if residuo == 7:
        valor_a_texto = "SIETE"
    if residuo == 8:
        valor_a_texto = "OCHO"
    if residuo == 9:
        valor_a_texto = "NUEVE"
    return valor_a_texto
 
if __name__ == '__main__':
    n = ingrese_numero()
    n = str(n)
    n = n[::-1]
    n = int(n)
    while(n>0):
        print(number_as_text(n),end=" ")
        n = n //10
        
    