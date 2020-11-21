class House:

    def __init__(self, address, elevator, flats, floors=5, sixth_floor=None):
        print("initialization")
        self.floors = floors
        self.address = address
        self.elevator = elevator
        self.flats = flats
        self.sixth_floor = sixth_floor
        self.rented = False


    def give_to_rent(self):
        self.rented = True
        return f"Дом {self.address}/{self.floors}в аренде"

    def fun(self):
        return "Text"

hryshevka = House("Токтогула 175", False, 100)
hryshevka2 = House("Манаса 61", True, 200, 9, True)

print(f"Лифт ? => {hryshevka.elevator}")
print(f"Этаж ? => {hryshevka.floors}")
print(f"Адрес ? => {hryshevka.address}")
print(f"Квартиры ? => {hryshevka.flats}")
print(f"Арендовано ? => {hryshevka.rented}")

print()
print(f"Лифт ? => {hryshevka2.elevator}")
print(f"Этаж ? => {hryshevka2.floors}")
print(f"Адрес ? => {hryshevka2.address}")
print(f"Квартиры ? => {hryshevka2.flats}")
print(f"Арендовано ? => {hryshevka2.rented}")

print(hryshevka.give_to_rent())
print(hryshevka2.give_to_rent())
