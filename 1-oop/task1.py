
# Герой, у которого есть имя, hp, inventory list и пометка жив ли он.
# Нужно сделать методы take_damage, heal, add_item, show_status.

class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.inventory: list[str] = []
        self.is_alive = True

    def take_damage(self, damage):
        if self.is_alive:
            self.hp -= damage
            if self.hp <= 0:
                self.is_alive = False
                print(f"{self.name} has died.")
            else:
                print(f"{self.name} took {damage} damage and has {self.hp} HP left.")
        else:
            print(f"{self.name} is already dead.")

    def heal(self, amount):
        if self.is_alive:
            self.hp += amount
            print(f"{self.name} healed for {amount} HP and now has {self.hp} HP.")
        else:
            print(f"{self.name} cannot be healed because they are dead.")

    def add_item(self, item):
        if self.is_alive:
            self.inventory.append(item)
            print(f"{item} added to {self.name}'s inventory.")
        else:
            print(f"{self.name} cannot carry items because they are dead.")

    def show_status(self):
        status = "alive" if self.is_alive else "dead"
        print(f"{self.name} is {status} with {self.hp} HP and has the following items: {', '.join(self.inventory)}")

hero = Hero("Arthur")
hero.add_item("Sword")
hero.take_damage(30)
hero.heal(20)
hero.take_damage(100)
