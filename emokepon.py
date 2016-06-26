import random
#-----------------------
#--DEFINE CLASS OF POKEMONS
#------------------------

class Pokemon():
    gotta_catch_em_all = "Yes you do."

    def __init__(self, colour, name, ouch_statement):
        self.health_points = random.randint(8,13)
        self.colour = colour
        self.name = name
        self.ouch_statement = ouch_statement

    def alive(self):
        return self.health_points > 0

    def attack(self, defender):
        if defender.alive():

            damage = random.randint(1,3)

            defender.health_points -= damage

            print("You attacked:", defender.name)
            print("{} took {} damage".format(defender.name.title(), damage))

            print("Their health points are: {}".format(defender.health_points))
            if defender.health_points < 3:
                print(defender.ouch_statement)
        else:
            print(random.choice(defender.phrases))
            print("You attacked the corpse of {}, you sicko.".format(defender.name))

        print()
        input("Press anything to go to the next round")

#--------------------------------
#--DEFINE CLASS OF TRAINER
#--------------------------------

#----------------------------------
#--INSTANTIATE CLASSES FOR EMOKEPONS
#---------------------------------
snorlax = Pokemon('yellow',"Snorlax", "I'm trying to sleep!", )
bulbasaur = Pokemon('green', "bulbasaur", "mrrrrrr :(",)
charmander = Pokemon('red', "charmander", "fizzzzzzle :<",)

#----------------------------------
#--ADD CLASSES TO ARRAY FOR RANDOM CHOICE
#---------------------------------
pokemons = [snorlax, bulbasaur, charmander]



#----------------------------------
#--WELCOME TO THE BATTLE
#---------------------------------
print("Welcome to Emokepon")
print("Snorlax's hit points are:", snorlax.health_points)
print("Bulbasaur's hit points are:", bulbasaur.health_points)
print("Charmander's hit points are:", charmander.health_points)

#----------------------------------
#--ROUND LOGIC
#---------------------------------

for round_number in range(10):
    print("\n---------Round {} ----------".format(round_number))

    attacker = random.choice(pokemons)
    print("The attacker is:", attacker.name)
    copy_pokemons = pokemons[:]
    copy_pokemons.remove(attacker)
    defender = random.choice(copy_pokemons)
    print("The defender is:", defender.name)

    attacker.attack(defender)
