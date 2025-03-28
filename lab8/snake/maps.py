
SIZE = 50

text_map = [[
    '################',
    '#..............#',
    '#..............#',
    '#..............#',
    '#..............#',
    '....########....',
    '................',
    '................',
    '................',
    '................',
    '....########....',
    '#..............#',
    '#..............#',
    '#..............#',
    '#..............#',
    '################',
    ], [
    '################',
    '#..............#',
    '#..............#',
    '#..............#',
    '#..............#',
    '#..............#',
    '#..............#',
    '#..............#',
    '#..............#',
    '#..............#',
    '#..............#',
    '#..............#',
    '#..............#',
    '#..............#',
    '#..............#',
    '################',
    ]
]

lvl_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == "#":
            lvl_map.add((i * SIZE, j * SIZE))