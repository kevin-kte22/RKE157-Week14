from file_utils import get_random_from_file
from character import Hero, Villain

hero_name = get_random_from_file(r'data\heroes.txt')
hero_weapon = get_random_from_file(r'data\weapons.txt')
villain_name = get_random_from_file(r'data\villains.txt')
villain_weapon = get_random_from_file(r'data\weapons.txt')

hero = Hero(hero_name, hero_weapon)
villain = Villain(villain_name, villain_weapon)

print("===BATTLE BEGINS===")

print(f"Hero: {hero.name} I Weapon: {hero.weapon} I HP: {hero.hp}")
print(f"Villain: {villain.name} I Weapon: {villain.weapon} I HP: {villain.hp}")

round_number = 1

while hero.is_alive() and villain.is_alive():
    print(f"===ROUND {round_number}===")

    hero.attack(villain)

    if not villain.is_alive():
        break

    villain.attack(hero)

    round_number += 1

print("===BATTLE ENDS===")

if hero.is_alive():
    print(f"{hero.name} saves the day")
else:
    print(f"{villain.name} has won the battle")