from classes.game import Person, Bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


# Create magic
fire = Spell("Fire", 25, 600, "blackMagic")
thunder = Spell("Thunder", 25, 400, "blackMagic")
blizzard = Spell("Blizzard", 25, 500, "blackMagic")
meteor = Spell("Meteor", 40, 2100, "blackMagic")
quake = Spell("Quake", 14, 430, "blackMagic")
cure = Spell("Cure", 25, 650, "whiteMagic")
cura = Spell("Cura", 50, 1500, "whiteMagic")

# Create items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hiPotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superPotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
megaElixir = Item("MegaElixir", "elixir", "Fully restore party's HP/MP", 100)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item": potion, "quantity": 15},
                {"item": hiPotion, "quantity": 10},
                {"item": superPotion, "quantity": 6},
                {"item": elixir, "quantity": 5},
                {"item": megaElixir, "quantity": 2},
                {"item": grenade, "quantity": 5}]

# Instantiate Players
player1 = Person("Lilu:",3260, 135, 300, 34, player_spells, player_items)
player2 = Person("Luci:",4160, 188, 311, 34, player_spells, player_items)
player3 = Person("NGSW:",2460, 200, 200, 34, player_spells, player_items)

enemy1 = Person("Magu", 13200, 725, 545, 25, [], [])
enemy2 = Person("Lego  ", 1200, 135, 560, 325, [], [])
enemy3 = Person("Stor  ", 1200, 135, 560, 325, [], [])

players = [player1, player2, player3]
enemies = [enemy2, enemy1, enemy3]

running = True
i = 0

print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACK!" + Bcolors.ENDC)

while running:
    print("========================================================================")

    print("\n")
    print("NAME                 HP                                      MP")
    for player in players:
        player.get_player_status()
    print("\n")

    for enemy in enemies:
        enemy.get_enemy_status()

    for player in players:
        player.choose_action()
        choice = input("    Choose an action: ") # The player is choosing his way of fighting
        index = int(choice) - 1 # In order to choose the correct action in list, identify the index of it

        # Player generating damage based on the chosen option
        if index == 0:
            dmg = player.generate_damage() # In range 50-70 (60-10; 60+10)
            enemy = player.choose_target(enemies)

            enemies[enemy].take_damage(dmg)
            print("You attacked " + enemies[enemy].name. replace("  ", "") + " for", dmg, "points of damage.")

            if enemies[enemy].get_hp() == 0: # Delete dead enemy from the list killed by an attack
                print(Bcolors.BOLD + enemies[enemy].name.replace("  ", "") + " has died." + Bcolors.ENDC)
                del enemies[enemy]
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose a magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp() # And based on the current MP,
            if spell.cost > current_mp:  # find out if the player can continue to cast spells
                print(Bcolors.FAIL + "\nNot enough MP!\n" + Bcolors.ENDC)
                continue # If not able, can continue to use "ATTACK" until battle is HP is 0

            player.reduce_mp(spell.cost) # Reduce the magic points (MP) by the spell that was cast

            if spell.type == "whiteMagic":
                player.heal(magic_choice)
                print(Bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), " HP" + Bcolors.ENDC)
            elif spell.type == "blackMagic":
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(magic_dmg)
                print(Bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), " points of damage to " + enemies[enemy].name.replace("  ", "") + Bcolors.ENDC)

                if enemies[enemy].get_hp() == 0: # Delete dead enemy from the list killed by a magic attack
                    print(Bcolors.BOLD + enemies[enemy].name.replace("  ", "") + " has died." + Bcolors.ENDC)
                    del enemies[enemy]
        elif index == 2:
            player.choose_items()
            item_choice = int(input("    Choose an item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(Bcolors.FAIL + "\n" + "None left..." + Bcolors.ENDC)
                continue
            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(Bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + Bcolors.ENDC)
            elif item.type == "elixir":
                if item.name == "MegaElixir":
                    for i in players:
                        i.hp = i.maxHP
                        i.mp = i.maxMP
                else:
                    player.hp = player.maxHP
                    player.mp = player.maxMP
                print(Bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + Bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(item.prop)
                print(Bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage to "+ enemies[enemy].name.replace("  ", "") + Bcolors.ENDC)

                if enemies[enemy].get_hp() == 0: # Delete dead enemy from the list killed by an item attack
                    print(Bcolors.BOLD + enemies[enemy].name.replace("  ", "") + " has died." + Bcolors.ENDC)
                    del enemies[enemy]

 # Enemy counter-attack
    enemy_choice = 1
    target = random.randint(0, 2)
    enemy_dmg = enemies[0].generate_damage()

    players[target].take_damage(enemy_dmg) # land an enemy attack on random target
    print("Enemy attacks for", enemy_dmg, " points of damage." )

# Determine when the battle is over
    defeated_players = 0
    defeated_enemies = 0

    for player in players:
        if player1.get_hp() == 0:
            defeated_players += 1

    for enemy in enemies:
        if enemies[0].get_hp() == 0:
            defeated_enemies += 1

    if defeated_enemies == 2:
        print(Bcolors.OKGREEN + "You Win!" + Bcolors.ENDC)
        running = False
    elif defeated_players == 2:
        print(Bcolors.FAIL + "Your enemies have defeated you!" + Bcolors.ENDC)
        running = False