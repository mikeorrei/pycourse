STARTING_HEALTH = 100

items = [
    {
        "name": "potion",
        "type": "healing",
        "value": 10,
        "weight": 0.3,
    },
    {
        "name": "high potion",
        "type": "healing",
        "value": 25,
        "weight": 0.6,
    },
    {
        "name": "elixir",
        "type": "healing",
        "value": 50,
        "weight": 0.95,
    },
    {
        "name": "strength",
        "type": "power_up",
        "value": 3,
        "weight": 0.8,
    },
    {
        "name": "haste",
        "type": "power_up",
        "value": 1,
        "weight": 0.8,
    },
]

MONSTERS = [
    {
        "name": "Ifrit",
        "health": 40,
        "moves": [
            {"name": "Slash", "dmg": 5},
            {"name": "Meteor", "dmg": 10},
        ],
        "items": [items[0], items[1], items[3]],
    },
    {
        "name": "Sheeva",
        "health": 25,
        "moves": [
            {"name": "Blizzard", "dmg": 6},
            {"name": "Diamond Dust", "dmg": 18},
        ],
        "items": [items[0], items[1], items[4]],
    },
    {
        "name": "Ramuh",
        "health": 30,
        "moves": [
            {"name": "Thunder", "dmg": 10},
            {"name": "Judgement", "dmg": 13},
        ],
        "items": [items[0], items[1], items[2], items[4]],
    },
    {
        "name": "Anima",
        "health": 50,
        "moves": [
            {"name": "Pain", "dmg": 12},
            {"name": "Oblivion", "dmg": 20},
        ],
        "items": [items[1], items[2], items[3], items[4]],
    },
]

PLAYER = {
    "health": 100,
    "basic": {
        "min": 4,
        "max": 8,
        "skip": 0,
        "cd": 0,
    },
    "heavy": {
        "min": 1,
        "max": 24,
        "skip": 1,
        "cd": 2,
    },
    "slam": {
        "min": 8,
        "max": 32,
        "skip": 2,
        "cd": 4,
    },
    items: [],
}