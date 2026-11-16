# adjacency list: each node -> its neighbours
tube = {
    "Kings Cross": ["Euston", "Angel", "Russell Sq"],
    "Euston": ["Kings Cross", "Warren St"],
    "Angel": ["Kings Cross", "Old St"],
    "Russell Sq": ["Kings Cross", "Holborn"],
    "Warren St": ["Euston", "Oxford Circus"],
    "Holborn": ["Russell Sq", "Oxford Circus"],
    "Old St": ["Angel"],
    "Oxford Circus": ["Warren St", "Holborn"],
}
