def dodaj(x, y):
    return x + y

def odejmij(x, y):
    return x - y

def mnoz(x, y):
    return x * y

def dziel(x, y):
    if y == 0:
        return "Nie można dzielić przez zero!"
    return x / y

def kalkulator():
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    while True:
        wybor = input("Wprowadź numer operacji (1/2/3/4): ")

        if wybor in ('1', '2', '3', '4'):
            try:
                a = float(input("Wprowadź pierwszą liczbę: "))
                b = float(input("Wprowadź drugą liczbę: "))
            except ValueError:
                print("Proszę wprowadzić poprawną liczbę.")
                continue

            if wybor == '1':
                print(f"Wynik: {dodaj(a, b)}")
            elif wybor == '2':
                print(f"Wynik: {odejmij(a, b)}")
            elif wybor == '3':
                print(f"Wynik: {mnoz(a, b)}")
            elif wybor == '4':
                print(f"Wynik: {dziel(a, b)}")
        else:
            print("Proszę wybrać poprawną opcję.")

if __name__ == "__main__":
    kalkulator()
