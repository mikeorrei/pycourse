mylist = [
    {'type': 'int', 'value': 5},
    {'type': 'add', 'value': '+'},
    {'type': 'int', 'value': 8},
    {'type': 'mul', 'value': '*'},
    {'type': 'int', 'value': 22},
    {'type': 'int', 'value': 2},
    {'type': 'sub', 'value': '-'},
    {'type': 'int', 'value': 16},
    {'type': 'int', 'value': 6},
    {'type': 'mul', 'value': '*'},
    {'type': 'int', 'value': 24},
    {'type': 'int', 'value': 4}
]

tok = mylist.pop(0)


tree = {
    'left': {
        'left': {'type': 'int', 'value': 5},
        'op': {'type': 'add', 'value': '+'},
        'right': {
            'left': {'type': 'int', 'value': 8},
            'op': {'type': 'mul', 'value': '*'},
            'right': {'type': 'int', 'value': 22}
        }
    },
    'op': {'type': 'sub', 'value': '-'},
    'right': {
        'left': {'type': 'int', 'value': 16},
        'op': {'type': 'mul', 'value': '*'},
        'right': {'type': 'int', 'value': 24}
    }
}