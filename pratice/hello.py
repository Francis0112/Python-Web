
# getter setter in java. rock and roll
class human():
    
    #empty constructor in java. 
    def __init__(self) -> None:
        self.__name=None
        self.__age=None
        self.__race=None
        self.__zombie=None

    def set_name(self, name):
        self.__name = name
    
    def set_age(self, age):
        self.__age = age

    def set_race(self, race):
        self.__race = race

    def set_zombie(self, zombie):
        self.__zombie = zombie

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_race(self):
        return self.__race
    
    def get_zombie(self):
        return self.__zombie

guy = human()
guy.set_name("francis")
guy.set_age(28)
guy.set_race("noypi")
guy.set_zombie(False)

print(guy.get_name(), guy.get_age(), guy.get_race(), guy.get_zombie())


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
print(pets("cat","doggie", "kon"))


# **kwargs
def lunch(**onegai):
    for k, v in onegai.items():
        print(f"{k}: {v}")

lunch(ulam="lawson pork steak", drinks="coke mismo", rice=2)

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