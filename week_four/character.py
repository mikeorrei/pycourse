from random import randint

class Character():
    def __init__(self, health: int, name: str):
        self.health = health
        self.name = name
        self.attacks = {}

    def create_attack(self, name: str, min_dmg: int, max_dmg: int):
        self.attacks[name] = {}
        self.attacks[name]["min"] = min_dmg
        self.attacks[name]["max"] = max_dmg

        # Creating the below dictionary:
        #
        # self.attacks = {
        #     "fireball" : {
        #         "min": 5,
        #         "max": 10
        #     }
        # }

    def deal_damage(self, name: str) -> (int | None):
        if name in self.attacks:
            try:
                dmg = randint(self.attacks[name]["min"], self.attacks[name]["max"])
                return dmg
            except Exception as e:
                print("Error: Attack requested does not have a min and/or max damage value")
                print(f"Exception: {e}")
            # Runs if the try succeeds
            # else:
            #     pass
            #
            # Runs no matter what
            # finally:
            #     pass
        else:
            print(f"Attack '{name}' does not exist in the character's attack pool")

    def is_alive(self) -> bool:
        if self.health > 0:
            return True
        else:
            return False


if __name__ == '__main__':
    test = Character(health=100, name="joe")

    if test.health > 0:
        print(f"Greater than 0")
