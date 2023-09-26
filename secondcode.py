def main(n):
    def is_even(n):
        if n%2 != 0:
            print("El numero es impar")
    def is_odd(n):
        if n%2 == 0:
            print("El numero es par")
    is_even(n)
    is_odd(n)
if __name__ == '__main__':
    main(5)