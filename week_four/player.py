from character import Character

# This is what the player's 'self.items' list of items will be structured
sample_items = [
{
    "name": "potion",
    "power": 15,
    "quantity": 0,
},
{
    "name": "high potion",
    "power": 35,
    "quantity": 0,
},
]

class Monster(Character):
    def __init__(self, health: int, name: str):
        super().__init__(health=health, name=name)

    def drop_item(self):
        pass

class Player(Character):
    def __init__(self, health: int, name: str):
        super().__init__(health=health, name=name)
        self.create_attack(name="slam", min_dmg=4, max_dmg=8)
        self.create_attack(name="fireball", min_dmg=2, max_dmg=16)
        self.items = []

    # Overrides the Character create_attack() method
    # def create_attack(self):
    #     pass

    def add_item(self, item: dict):
        for i in range(0, len(self.items)):
            if item["name"] == self.items[i]["name"]:
                self.items[i]["quantity"] += 1
                return None
            
        self.items.append(
            {
                "name": item["name"],
                "power": item["power"],
                "quantity": 1
            }
        )

    def consume_healing_item(self, name: str):
        for i in range(0, len(self.items)):
            if name == self.items[i]["name"]:
                heal = self.items[i]["power"]
                self.items[i]["quantity"] -= 1
                break
        else:
            print(f"Iem not found in inventory")
            return None
        
        if self.health + heal > 100:
            self.health = 100
        else:
            self.health += heal


if __name__ == '__main__':
    player = Player(health=100, name="mike")

    player.add_item()

    monster = Monster(health=10, name="ifrit")
    monster.create_attack()
        
