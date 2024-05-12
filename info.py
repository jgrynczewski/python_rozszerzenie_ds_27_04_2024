# Rodzaje błędów
# 1. Błędy składniowe
# 2. Błędy czasu wykonywania - wyjątkami
# 3. Błędy logiczne

print("Ala ma kota")
x = 5

class A:
    def speak(self):
        print("hihihi")


def func():
    try:
        print("asd" + 2)
    except:
        print("Ok znalazłem błąd. Idę dalej.")
    print("Hello")



#######
z = func()
