
import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power = 20

    def attack(self, other):
        other.health -= self.power
        print(f"{self.name} наносит удар по {other.name}. \nУ {other.name} осталось {other.health} здоровья.")

    def alive(self):
        return self.health > 0

class Game:
    def __init__(self, name_2):
        self.name_2 = Hero(name_2)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Начало игры!")
        while self.name_2.alive() and self.computer.alive():
            if random.choice([True, False]):
                self.name_2.attack(self.computer)
            else:
                self.computer.attack(self.name_2)

            if not self.computer.alive():
                print(f"\n{self.computer.name} побеждён! {self.name_2.name} победил!")
                break
            elif not self.name_2.alive():
                print(f"\n{self.name_2.name} побеждён! {self.computer.name} победил!")
                break

# Начало игры
name_1 = input("Введите имя вашего игрока: ")
game = Game(name_1)
game.start()