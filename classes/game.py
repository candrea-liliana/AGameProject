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
    def __init__(self, hp, mp, atk, df, magic):
        self.maxHP = hp
        self.hp = hp
        self.maxMP = mp
        self.mp = mp
        self.atkLow = atk - 10
        self.atkHigh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

# Generate random damage
    def generate_damage(self):
        return random.randrange(self.atkLow, self.atkHigh)

    def generate_spell_damage(self, i):
        magic_low = self.magic[i]["dmg"] - 5
        magic_high = self.magic[i]["dmg"] + 5

        return random.randrange(magic_low, magic_high)

    def take_damage(self, dmg):
        self.hp -= dmg

        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp -= dmg
        if self.hp > self.maxHP:
            self.hp = self.maxHP

# Additional utility classes
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

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_magic_cost(self, i):
        return self.magic[i]["cost"]

# Action classes to choose for person
    def choose_action(self):
        i = 1
        print(Bcolors.OKBLUE + Bcolors.BOLD + "Actions" + Bcolors.ENDC)
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print(Bcolors.OKBLUE + Bcolors.BOLD + "Magic" + Bcolors.ENDC)
        for spell in self.magic:
            print(str(i) + ":", spell["name"], "(cost:", str(spell["cost"]) + ")")
            i += 1