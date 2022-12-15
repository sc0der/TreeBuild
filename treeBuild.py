def tree_builder(source: list):
    i = 0
    root = dict()
    node = root
    while i < len(source):
        parent = source[i][0]
        child = source[i][1]
        if parent is None:
            root.update({child: {}})
            i += 1

        else:
            node[parent].update({child: {}})
            if i != len(source) - 1 and source[i+1][0] in root:
                node = root
            elif i != len(source) - 1 and source[i+1][0] != parent:
                node = node[parent]
            i += 1

    return root

source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]


expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}

if __name__ == '__main__':
    assert tree_builder(source) == expected
