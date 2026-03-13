import random
import time

index = [
    {
        "name": "Slag",
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
        "name": "Epstein",
        "damage": 1000000,
        "cost": 67  
    },
]

stålar = 20
hp_player = 100
hp_monster = 100

print("--- FIGHT START ---")
while hp_player > 0 and hp_monster > 0:
    choice_input = input("Vilken attack vill du använda? ").strip()
    
    attack = None
    for a in index:
        if a["name"].lower() == choice_input.lower():
            attack = a
            break
    
    if attack:
        if attack["cost"] <= stålar:
            skada = attack["damage"]
            hp_monster -= skada
            stålar -= attack["cost"]
            time.sleep(1)
            print(f"Du använder {attack['name']}! Monstern tar [{skada}] skada.")
        else:
            time.sleep(0.5)
            print(f"Hell nah fattig-lap! Glömt hur många stålar du har, hmm? Du har bara [{stålar}] stålar polarn.")
            time.sleep(3)
            print("Du vet vad, av med turen")
    else:
        print(f"Ogiltig attack: '{choice_input}'. Försök igen.")

    if hp_monster > 0:
        dmg_monster = random.randint(5, 15)
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