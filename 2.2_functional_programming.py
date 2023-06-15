scientists = [
    {'name': 'Ada Lovelace', 'field': 'math', 'born': 1815, 'nobel': False},
    {'name': 'Emmy Noether', 'field': 'math', 'born': 1882, 'nobel': False}
]

# mutable data structure - We can just rename names; example: Ada
scientists[0]['name'] = 'Ed Lovelace'


import collections
Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel',
])

# Create Scientist object
ada = Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False)

# Reach into Scientist object
print(ada.name)

print(ada.field)

# immutable data structure - We can't rename names; example: Ada
#ada.name = 'Ed Lovelace' # Error: AttributeError: can't set attribute


# Mixing data structures
scientists = [
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
]

# immmutable data structure - We can just rename names; example: Ada
#scientists[0].name = 'Ed Lovelace'

# mutable data structure - We can delete scientists from the list
del scientists[0]

print(scientists)


# Tuple
scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)

# can't delete scientists from the tuple
#del scientists[0]

# cant add scientists to the tuple
# scientists.append(Scientist(name='Sally Ride', field='physics', born=1951, nobel=False))