from random import randint
import visuals

class Character:
    def __init__(self, name, attack_strength, defence_strength, max_hp):
        self.name = name
        self.attack_strength = attack_strength
        self.defence_strength = defence_strength
        self.max_hp = max_hp
        self.hp = max_hp

    def attack(self, opponent):
        """
        Deals damage to opponent
        """
        attack_hit_or_miss = randint(0,4)
        if attack_hit_or_miss == 0:
            print('attack missed')
        else:
            random_damage_value = randint(-1,2) 

            opponent.receive_damage(self.attack_strength + random_damage_value - opponent.defence_strength)
            if opponent.hp >0:
                print(f'{self.name} attacked {opponent.name} who now has {opponent.hp} hp')
            elif opponent.hp <= 0:
                print(f'{self.name} defeated {opponent.name} who is now dead. {self.name} has won the contest')
                visuals.win_visual()  # WHY NOT WORKING 

    def receive_damage(self, damage_amount):
        """
        Removes amount of damage recieved from own hp. If hp is 0 character dies and is remove from the game
        """
        self.hp = self.hp - damage_amount
        #  Would be nice to add a delete self but how to make this work?

    def character_details(self):
        """
        Gives the name, hp, attack_strength and defence_strength of the character 
        """
        return(
            f'{self.name} has {self.hp} hp, {self.attack_strength} attack_strength and {self.defence_strength} defence_strength'
        )

class Goblin(Character):
    GOBLIN_TYPES = ("fire", "water", "forest")

    def __init__(self, name, goblin_type, attack_strength=5, defence_strength=3, max_hp=10):
        super().__init__(name, attack_strength, defence_strength, max_hp)
        if (not goblin_type in Goblin.GOBLIN_TYPES):
            raise ValueError(f'{goblin_type} is not a valid goblin type. Choose one of "fire", "water" or "forest" '
            )
        else:
            self.goblin_type = goblin_type
        
        print(f'{self.name} the {self.goblin_type} goblin has been created')
        visuals.goblin_visual()

    def __str__(self): #  DUPLICATE FUNCTION - PARSE TEXT OF NAME AND PUT THIS IN CHARACTER CLASS
        """
        When object is printed returns name and goblin type 
        """
        return f'{self.name} ({self.goblin_type} goblin)'

    def healing_spell(self):
        """
        Increases own health by 2 up to a maximum of max_hp
        """
        if self.hp == self.max_hp:
            print(f'{self.name} does not need healing spell as hp is max')
        elif self.hp == self.max_hp-1:
            self.hp+=1
            print(f'{self.name} used heal spell and now has max hp')            
        else:
            self.hp+=2
            if self.hp == self.max_hp:
                print(f'{self.name} used heal spell and now has max hp')
            else:
                print(f'{self.name} used heal spell and now has {self.hp} hp')

    @classmethod
    def getGoblinTypes(cls):
        """
        Returns the possible goblin types
        """
        return cls.GOBLIN_TYPES

class Gladiator(Character):

    def __init__(self, name, attack_strength=6, defence_strength=2, max_hp=11):
        super().__init__(name, attack_strength, defence_strength, max_hp)

        print(f'{self.name} the gladiator has been created')
        visuals.gladiator_visual()

    def __str__(self): #  DUPLICATE FUNCTION - PARSE TEXT OF NAME AND PUT THIS IN CHARACTER CLASS
        """
        When object is printed returns name and goblin type 
        """
        return f'{self.name} ({self.goblin_type} goblin)'

    def berserk_attack(self, opponent): #  CAN THIS INHERET FROM ATTACK FUNCTION?
        """
        Deals high amount damage to opponent and also damage to self
        """
        attack_hit_or_miss = randint(0,4)
        if attack_hit_or_miss == 0:
            print('attack missed')
        else:
            random_damage_value_self = randint(-1,2)
            random_damage_value_opponent = randint(-1,2)

            combined_damage_value = self.attack_strength + random_damage_value_opponent - opponent.defence_strength
            opponent.receive_damage(combined_damage_value)
            recoil_damage = self.attack_strength + random_damage_value_self -5
            print(f'{self.name} has recieved {recoil_damage} recoil damage from beserk attack')  # Damage statement comes before any other statement if character dies
            self.receive_damage(recoil_damage)
            
            if self.hp <=0 and opponent.hp <=0:
                print(f'{self.name} killed {opponent.name} but died in the process so the fight is a draw')
            elif opponent.hp <= 0:
                print(f'{self.name} defeated {opponent.name} who is now dead. {self.name} has won the contest')
                visuals.win_visual()
            elif self.hp <= 0:
                print(f'{self.name} killed itself so {opponent.name} wins the fight')
                visuals.win_visual()
            else:
                print(f'{self.name} attacked {opponent.name} who now has {opponent.hp} hp')

if __name__ == '__main__':
    fire_boy = Gladiator('fire_boy', 'fire')
    forest_boy = Gladiator('foresto')

    print(forest_boy.character_details())

    forest_boy.attack(fire_boy)

    forest_boy.berserk_attack(fire_boy)
    forest_boy.attack(fire_boy)
    forest_boy.attack(fire_boy)

    

  