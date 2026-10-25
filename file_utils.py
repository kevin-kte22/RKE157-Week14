import random

def get_random_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    items = []

    for line in lines:
        new_item = line.strip()
        items.append(new_item)

    random_item = random.choice(items)
    
    return random_item