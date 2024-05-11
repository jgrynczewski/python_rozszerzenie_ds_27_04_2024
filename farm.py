# nazewnictwo klas
# zmienne, funkcje, pliki (moduły), foldery (pakiety) nazywa zgodnie z konwencją snake case moja_nowa_zmienna
# klasy nazywamy zgodnie z konwencja CamelCase - MojaNowaKlasa
# ciekawoskta: (upper camel case - MojaNazwaKlasy, lower camel case (aka pascal case) mojaNazwaKlasy

# DRY - Don't Repeat Yourself

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

    # dependency (USE-A) - używa, zależności
    def turn_on_the_ligth(self, lamp):
        lamp.turn_on()


class Lamp:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False


#############################################################################
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

lamp1 = Lamp()
print(lamp1.is_on)
cow2.turn_on_the_ligth(lamp1)
print(lamp1.is_on)