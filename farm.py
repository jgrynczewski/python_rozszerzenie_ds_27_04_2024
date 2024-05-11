# nazewnictwo klas
# zmienne, funkcje, pliki (moduły), foldery (pakiety) nazywa zgodnie z konwencją snake case moja_nowa_zmienna
# klasy nazywamy zgodnie z konwencja CamelCase - MojaNowaKlasa
# ciekawoskta: (upper camel case - MojaNazwaKlasy, lower camel case (aka pascal case) mojaNazwaKlasy

# definicja klasy Cow
class Cow:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.is_alive = True

    # metoda
    def give_a_voice(self, suffix):
        if self.is_alive:
            print(f"Muuuuuuuuu {suffix}")
        else:
            print("R.I.P")

    def kill_yourself(self):
        self.is_alive = False
        print("Umieram")


# inicjalizacja obiektu klasy Cow
cow1 = Cow("Mućka")
print(cow1.name)
print(cow1.age)

cow1.give_a_voice("tralala")
cow1.give_a_voice("bum tara bum")

cow2 = Cow("Milka", age=2)
print(cow2.name)
print(cow2.age)

cow1.kill_yourself()
cow1.give_a_voice("Hahaha, żartowalam")