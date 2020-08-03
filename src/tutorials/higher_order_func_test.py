b = lambda x: -x[0]
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=b)
print(pairs)
