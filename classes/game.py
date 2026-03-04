import random


# Helper class to print colored output for CMD Line
class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self,name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxHP = hp
        self.hp = hp
        self.maxMP = mp
        self.mp = mp
        self.atkLow = atk - 10
        self.atkHigh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

# Generate random damage
    def generate_damage(self):
        return random.randrange(self.atkLow, self.atkHigh)

    def take_damage(self, dmg):
        self.hp -= dmg

        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp -= dmg

        if self.hp > self.maxHP:
            self.hp = self.maxHP

# Additional utility functions
    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxHP

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxMP

    def reduce_mp(self, cost):
        self.mp -= cost

# Action classes to choose for person
    def choose_action(self):
        i = 1

        print("\n" + "    " + Bcolors.BOLD + self.name + Bcolors.ENDC)
        print(Bcolors.OKBLUE + Bcolors.BOLD + "    ACTIONS" + Bcolors.ENDC)
        for item in self.actions:
            print("        " + str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1

        print("\n" + Bcolors.OKBLUE + Bcolors.BOLD + "    MAGIC" + Bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_items(self):
        i = 1

        print("\n" + Bcolors.OKBLUE + Bcolors.BOLD + "    ITEMS" + Bcolors.ENDC)
        for item in self.items:
            print("        " + str(i) + ".", item["item"].name + ":", item["item"].description, " (x" + str(item["quantity"]) + ")")
            i += 1

    def get_player_status(self):
        # Calculate HP/MP progress bars
        hp_bar = ""
        hp_ticks = (self.hp / self.maxHP) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.maxMP) * 100 / 10

        while hp_ticks > 0:
            hp_bar += "█"
            hp_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        # Dynamic progress values to display for HP/MP
        hp_string = str(self.hp) + "/" + str(self.maxHP)
        current_hp = ""

        if len(hp_string) > 0:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxMP)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)

            while decreased > 0:
                current_mp += " "
                decreased -= 1
            current_mp += mp_string
        else:
            current_mp = mp_string

        print("                     _________________________               __________")
        print(Bcolors.BOLD + self.name + "     " +
              current_hp + " |" + Bcolors.OKGREEN + hp_bar + Bcolors.ENDC + "|     " +
              current_mp + " |" + Bcolors.OKBLUE + mp_bar + Bcolors.ENDC + "|")

    def get_enemy_status(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxHP) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxHP)
        current_hp = ""

        if len(hp_string) > 0:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                      __________________________________________________")
        print(Bcolors.BOLD + self.name + "     " +
              current_hp + " |" + Bcolors.FAIL + hp_bar + Bcolors.ENDC + "|")