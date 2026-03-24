import random
import time

index = [
    {
        "name": "Dodge",
        "damage": 0,
        "cost": 7
    },
    {
        "name": "Gräva efter Guld",
        "damage": 0,
        "cost": -10
    },
    {
        "name": "Slap",
        "damage": 5,
        "cost": 0
    },
    {
        "name": "Eldklot",
        "damage": 20,
        "cost": 10
    },
    {
        "name": "67",
        "damage": 67,
        "cost": 30
    },
    {
        "name": "Heavenly Aura",
        "damage": -10,
        "cost": 10
    },
    {
        "name": "kys",
        "damage": 1000000,
        "cost": 67  
    },
]

pekomon=[
    {
        "name": "pikaong",
        "hp": 40,
        "attacks": [
            {"name": "Dhunder shock", "power": 20},
            {"name": "dih", "power": 25}
        ],
    },
    {
        "name": "Hjalmar",
        "hp": 67,
        "attacks": [
            {"name": "Flex Muscle", "power": 67},
            {"name": "cykel", "power": 10}
        ],
    },
    {
        "name": "Bulba-MAN",
        "hp": 150,
        "attacks": [
            {"name": "Overgrow", "power": -10},
            {"name": "Sallad dih", "power": 49}
        ],
    },
]

monster = random.choice(pekomon)
stålar = 0
hp_player = 100
hp_monster = monster['hp']

print("--- FIGHT START ---")

print(f"A wild {monster['name']} appeared!")
print(f"HP: {monster['hp']}")

while hp_player > 0 and hp_monster > 0:
    choice_input = input("Vilken attack vill du använda? ").strip()
    
    attack = None
    for a in index:
        if a["name"].lower() == choice_input.lower():
            attack = a
    
    if attack:
        if attack["cost"] <= stålar:
            crit_player = random.randint(1,10)
            stålar -= attack["cost"]
            skada = attack["damage"]
            if crit_player == 10:
                skada *= 2
            if skada<0:
                hp_player -= skada
                print(f"Du använder {skada}! Du Healar [{skada}] skada.")
            else:
                hp_monster -= skada
                print(f"Du använder {skada}! Monstern tar [{skada}] skada.")
        else:
            time.sleep(0.5)
            print(f"Hell nah fattig-lap! Glömt hur många stålar du har, hmm? Du har bara [{stålar}] stålar polarn.")
            time.sleep(3)
            print("Du vet vad, av med turen")
    else:
        print(f"Ogiltig attack: '{choice_input}'. Försök igen.")

    if hp_monster > 0:
        if attack and attack["name"] == "Dodge":
            print("Wowswers skidido du Dodgade och tog inge damage!")
        else:
            dmg_monster = monster["attacks"]["power"]
            crit_monster = random.randint(1,10)
            if crit_monster == 10:
                hp_player -= dmg_monster*2
                print(f"Monstret CRIT-ar dig! Du tar [{dmg_monster*2}] skada.")
            else:
                hp_player -= dmg_monster
                time.sleep(0.5)
                print(f"Monstret biter dig! Du tar [{dmg_monster}] skada.")
    
    stålar += 10
    time.sleep(1)
    print("Du får 10 stålar")
    time.sleep(0.5)
    print(f"Din HP: {hp_player} | Monster HP: {hp_monster} | Du har {stålar} stålar nu\n") 
    time.sleep(1)   


if hp_player > 0:
    print("Du vann!")
else:
    print("Du dog...")