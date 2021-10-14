class House:
    doors: int
    color: str
    def __init__(self, doors: int, color: str)-> None:
        self.doors = doors
        self.color = color
    def change_color(self, new_color: str)-> None:
        if new_color == self.color:
            print("Nowy kolor nie moze byc taki sam jak stary kolor")
            return
        self.color = new_color
    def __str__(self)-> str:
            return f'liczba drzwi: {self.doors},'
            f'kolor elewacji: {self.color}'
green_house: House = House(doors=30, color="green")
print(green_house.doors)

