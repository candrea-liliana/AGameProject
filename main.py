from classes.game import Person, Bcolors
from classes.magic import Spell

#Create Black magic
fire = Spell("Fire", 10, 100, "blackMagic")
thunder = Spell("Thunder", 10, 100, "blackMagic")
blizzard = Spell("Blizzard", 10, 100, "blackMagic")
meteor = Spell("Meteor", 30, 200, "blackMagic")
quake = Spell("Quake", 12, 130, "blackMagic")

# Create White magic
cure = Spell("Cure", 12, 80, "whiteMagic")
cura = Spell("Cura", 18, 100, "whiteMagic")

# Instantiate People
player = Person(460, 65, 60, 34, [fire, thunder, blizzard, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0

# Bcolors.ENDC - Specify where the style ends
print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACK!" + Bcolors.ENDC)

while running:
# Player landing an attack
    # The player is choosing his way of fighting
    print("============================")
    player.choose_action()
    choice = input("Choose an action: ")
    index = int(choice) - 1 # in order to choose the correct action in list, identify the index of it

    # Player generating damage based on the chosen option
    if index == 0: # Attack
        dmg = player.generate_damage() # in range 50-70 (60-10; 60+10)
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.")
    elif index == 1: # If Magic, then
        player.choose_magic()
        magic_choice = int(input("Choose a magic: ")) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        # And based on the current MP,
        # find out if the player can continue to cast spells
        current_mp = player.get_mp()
        if spell.cost > current_mp:
            print(Bcolors.FAIL + "\nNot enough MP!\n" + Bcolors.ENDC)
            continue #  If not able, can continue to use "ATTACK" instead and the battle goes on

        # Reduce the magic points (MP) by the spell that was cast
        player.reduce_mp(spell.cost)
        enemy.take_damage(magic_dmg)
        print(Bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage!" + Bcolors.ENDC)

 # Enemy counter-attack
    enemy_choice = 1 # For attacking the player

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "points of damage." )

    print("______________________________________")
    print("Enemy HP:", Bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + Bcolors.ENDC + "\n")

    print("Your HP:", Bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + Bcolors.ENDC)
    print("Your MP:", Bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + Bcolors.ENDC + "\n")

# Determine when the battle is over
    if enemy.get_hp() == 0:
        print(Bcolors.OKGREEN + "You Win!" + Bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(Bcolors.FAIL + "Your enemy has defeated you!" + Bcolors.ENDC)
        running = False