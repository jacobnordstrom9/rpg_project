# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Characters():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print("{} does {} damage to the {}.".format(self.name, self.power, enemy.name))

    def alive(self):
        if self.health > 0:
            return True
        return False
    
    def print_status(self):
        print("{} currently has {} health and {} power".format(self.name, self.health, self.power))  

def main():
    hero = Characters("Hero", 10, 0)
    goblin = Characters("Goblin", 6, 2)
    zombie = Characters("Zombie", 100, 5)

    while hero.alive():
        print()
        hero.print_status()
        zombie.print_status()
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(zombie)
            if zombie.health <= 0:
                print("The zombie is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0:
            # Goblin attacks hero
            zombie.attack(hero)
            if hero.health <= 0:
                print("You are dead.")

main()