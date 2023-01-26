
# getter setter in java. rock and roll
class character():
    
    #empty constructor in java. 
    def __init__(self) -> None:
        self.__name=None
        self.__race=None
        self.__weapon=None
        self.__combat=None

    def set_name(self, name):
        self.__name = name
    
    def set_race(self, race):
        self.__race = race

    def set_weapon(self, weapon):
        self.__weapon = weapon

    def set_combat(self, combat):
        self.__combat = combat

    def get_name(self):
        return self.__name
    
    def get_race(self):
        return self.__race
    
    def get_weapon(self):
        return self.__weapon
    
    def get_combat(self):
        return self.__combat


char1 = character()
char1.set_name("player1")
char1.set_race("tank")
char1.set_weapon("hammer")
char1.set_combat("mellee")
print(char1.get_name(), char1.get_race(), char1.get_weapon(), char1.get_combat())

char2 = character()
char2.set_name("player2")
char2.set_race("mage")
char2.set_weapon("wand")
char2.set_combat("range")
print(char2.get_name(), char2.get_race(), char2.get_weapon(), char2.get_combat())


# *args
def add(*args):
    total = 0
    for i in args:
        total = total+i
    return total


def pets(*args):
    fav = ""
    for i in args:
        fav +=f"hello konichiwa {i} \n"
    return fav

print(add(10,10,30))
print(pets("cat","doggie", "bird"))


# **kwargs
def lunch(**onegai):
    for k, v in onegai.items():
        print(f"{k}: {v}")

lunch(ulam="lawson pork steak", rice=2, drinks="coke mismo")

# random drop item from a boss monster MMORPG
import random

character_class = "Wizard"
relic = ["invisibility cloak", "dagger of escape", "ring of health", None]
rare_weapon = ["epic sword", "epic bow", "epic blade", "epic staff", None]
not_rare_item = ["silver cup","plate","coins","boots","dirty rug"]

boss_drop_relic = random.choice(relic)
boss_drop_weapon = random.choice(rare_weapon)
boss_drop_item = random.choice(not_rare_item)

loot = []
loot.append(boss_drop_relic)
loot.append(boss_drop_weapon)
loot.append(boss_drop_item)
print(loot)