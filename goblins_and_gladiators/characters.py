from random import randint
import visuals
from abc import ABC, abstractmethod


class Character(ABC):
    __character_list = None  # Used in static method to return created characters

    def __init__(self, name, attack_strength, defence_strength, max_hp, item=""):
        """
        Constructor class that initiates Character objects
        """
        self.name = name
        self.attack_strength = attack_strength
        self.defence_strength = defence_strength
        self.max_hp = max_hp
        self.hp = max_hp  # Current hp can be equal to or less than max hp
        self.item = (
            item  # The character has no item as default but can equip up to 1 item
        )

    def attack(self, opponent):
        """
        Deals damage to opponent, note attack has random chance of missing and dealing 0 damage

        Parameters
        ----------
        opponent
            The character affected (Character)

        Returns
        --------
            If the attack is successfull, opponent receives damage from the attack. The amount of 
            damage dealt is equal to the attack_strength attacking character + randomized value 
            - defence_strength of defending chatacter. If the attack misses a string is printed to 
            notify attack has missed and no damage is dealt 
        """
        if self == opponent:
            print(f"{self.name} cannot attack itself, enter a different target")
            return None
        else:
            attack_hit_or_miss = randint(0, 4)  # Attack has random chance of missing
            if attack_hit_or_miss == 0:
                print("attack missed")
            else:
                random_damage_value = randint(
                    -1, 2
                )  # Random number altering the strength of attack

                opponent.receive_damage(
                    self.attack_strength
                    + random_damage_value
                    - opponent.defence_strength
                )
                if opponent.hp > 0:
                    print(
                        f"{self.name} attacked {opponent.name} who now has {opponent.hp} hp"
                    )
                elif opponent.hp <= 0:
                    print(
                        f"{self.name} defeated {opponent.name} who is now dead. {self.name} has won the contest"
                    )
                    visuals.win_visual()

    def equip_item(self, attatch_item):
        """
        Equips selected item to character

        Parameters
        ----------
        attatch_item
            The item the character is equipping (Item)
        
        Returns
        -------
            The character with its equipped item local parameter equal to the item name. This allows
            the character to use the equipped item
        """
        self.item = attatch_item.name
        print(f"{self.name} has now equipped {attatch_item.name}")

    def receive_damage(self, damage_amount):
        """
        Removes amount of damage recieved from own hp

        Parameters
        ----------
        damage_amount
            The amount of damage to recieve (int)

        Returns
        -------
            The character with damage_amount subtracted from its hp
        """
        self.hp = self.hp - damage_amount

    def character_details(self):
        """
        Gives key character details in a human readable sentence (more information than __str__)
        
        Returns
        --------
            The name, hp, attack_strength and defence_strength of the character 
        """
        return f"{self.name} has {self.hp} hp, {self.attack_strength} attack_strength and {self.defence_strength} defence_strength"

    @staticmethod
    def get_character_list():
        """
        Ensures only a singleton list of characters 

        Example
        -------
            the_characters = Character.get_character_list()
            the_characters.append(new_goblin_character)
            the_characters.append(new_gladiator_character)
            print(the_characters)
        """
        if Character.__character_list == None:
            Character.__character_list = []
        return Character.__character_list


class Goblin(Character):
    GOBLIN_TYPES = ("fire", "water", "forest")

    def __init__(
        self,
        name,
        goblin_type,
        attack_strength=5,
        defence_strength=3,
        max_hp=10,
        item="",
    ):
        """
        Constructor class that initiates Goblin objects
        """
        super().__init__(name, attack_strength, defence_strength, max_hp, item)
        if (
            not goblin_type in Goblin.GOBLIN_TYPES
        ):  #  A goblin must be created with a valid type
            raise ValueError(
                f'{goblin_type} is not a valid goblin type. Choose one of "fire", "water" or "forest"'
            )
        else:
            self.goblin_type = goblin_type

        print(f"{self.name} the {self.goblin_type} goblin has been created")
        visuals.goblin_visual()  #  Printing the visual graphic of a goblin

    def __str__(self):
        """
        Prints gobling objects name and type
        """
        return f"{self.name} ({self.goblin_type} goblin)"

    def __repr__(self):
        """
        Prints goblin objects information
        """
        return f'Goblin("{self.name}", {self.goblin_type}, {self.attack_strength}, {self.defence_strength}, {self.max_hp})'

    def character_details(self):
        """
        Gives key character details in a human readable sentence (more information than __str__)
        
        Returns
        --------
            The name, type, hp, attack_strength and defence_strength of the goblin character 
        """
        return f"{self.name} the {self.type} goblin has {self.hp} hp, {self.attack_strength} attack_strength and {self.defence_strength} defence_strength"

    def healing_spell(self):
        """
        Increases own health by up to 2 up to a maximum of max_hp

        Returns
        -------
            Goblin is returned with hp increased by up to 2 up to a maximum of max_hp
        """
        if self.hp == self.max_hp:
            print(f"{self.name} does not need healing spell as hp is max")
        elif self.hp == self.max_hp - 1:
            self.hp += 1
            print(f"{self.name} used heal spell and now has max hp")
        else:
            self.hp += 2
            if self.hp == self.max_hp:
                print(f"{self.name} used heal spell and now has max hp")
            else:
                print(f"{self.name} used heal spell and now has {self.hp} hp")

    def type_spell(self):
        """
        Depending on goblin type improves attack_strength, defence_strength or hp (and max_hp)

        Returns
        -------
        If goblin is fire type its attack_strength is increased by 1. If goblin is forest type 
        its defence_strength is increased by 1. If goblin is type water its hp is increased by 1, 
        note this also increases its max_hp by 1
        """
        if self.goblin_type == "fire":  # Fire type gets one additional attack_strength
            self.attack_strength += 1
            print(
                f"{self.name} used type spell and its attack strength increased to {self.attack_strength}"
            )
        elif (
            self.goblin_type == "forest"
        ):  # Forest type gets one additional defence_strength
            self.defence_strength += 1
            print(
                f"{self.name} used type spell and its defence strength increased to {self.attack_strength}"
            )
        else:  # Water type gets one additional hp (note this also increases max hp)
            self.hp += 1
            self.max_hp += 1
            print(
                f"{self.name} used type spell and its max hp increased to {self.max_hp}"
            )

    @classmethod
    def get_goblin_types(cls):
        """
        Gives available goblin types

        Returns
        -------
            A list of strings which shows all available goblin types
        """
        print(
            f"Available goblin types are {cls.GOBLIN_TYPES[0]}, {cls.GOBLIN_TYPES[1]} and {cls.GOBLIN_TYPES[2]}"
        )


class Gladiator(Character):
    def __init__(self, name, attack_strength=6, defence_strength=2, max_hp=11, item=""):
        """
        Constructor class that initiates Gladiator objects
        """
        super().__init__(name, attack_strength, defence_strength, max_hp, item)

        print(f"{self.name} the gladiator has been created")
        visuals.gladiator_visual()

    def __str__(self):
        """
        Prints gladiator objects name
        """
        return f"{self.name} (gladiator)"

    def __repr__(self):
        """
        Prints gladiator objects information
        """
        return f'Gladiator("{self.name}", {self.attack_strength}, {self.defence_strength}, {self.max_hp})'

    def berserk_attack(self, opponent):
        """
        Deals high amount of damage to opponent, and also damage to self. Note attack has 
        random chance of missing and dealing 0 damage to either party

        Parameters
        ----------
        opponent
            The character affected (Character)

        Returns
        --------
            If the attack is sucessfull, opponent receives damage from the attack. The amount of 
            damage dealt is equal to the attack_strength attacking character + randomized value 
            - defence_strength of defending chatacter. Note the character who attacks also recieves 
            its own attack_strength + randomized value -5 damage. If the attack misses a string is 
            printed to notify attack has missed and no damage is dealt to either character
        """
        if self == opponent:
            print(f"{self.name} cannot attack itself, enter a different target")
            return None
        else:
            attack_hit_or_miss = randint(0, 4)  #  Attack has random chance of missing
            if attack_hit_or_miss == 0:
                print("attack missed")
            else:
                random_damage_value_self = randint(
                    -1, 2
                )  #  Random value added to damage to self
                random_damage_value_opponent = randint(
                    -1, 2
                )  #  Random value added to damage to opponent

                combined_damage_value = (
                    self.attack_strength
                    + random_damage_value_opponent
                    - opponent.defence_strength
                )
                opponent.receive_damage(combined_damage_value)
                recoil_damage = self.attack_strength + random_damage_value_self - 5
                print(
                    f"{self.name} has recieved {recoil_damage} recoil damage from beserk attack"
                )  # Damage statement comes before any other statement if character dies
                self.receive_damage(recoil_damage)

                if self.hp <= 0 and opponent.hp <= 0:
                    print(
                        f"{self.name} killed {opponent.name} but died in the process so the fight is a draw"
                    )
                elif opponent.hp <= 0:
                    print(
                        f"{self.name} defeated {opponent.name} who is now dead. {self.name} has won the contest"
                    )
                    visuals.win_visual()
                elif self.hp <= 0:
                    print(
                        f"{self.name} killed itself so {opponent.name} wins the fight"
                    )
                    visuals.win_visual()
                else:
                    print(
                        f"{self.name} attacked {opponent.name} with berserk attack, {opponent.name} who now has {opponent.hp} hp"
                    )


class Item(ABC):
    ITEM_TYPES = ("amulet", "armour")  # The available item types in the game
    __item_list = None  # Used in static method to return created items

    def __init__(self, name):
        """
        Constructor class that initiates Item objects
        """
        self.name = name

    @abstractmethod
    def use_item(self, user_character):
        """
        Item is used on chatacter to modify the characters stats
        """
        return None

    @classmethod
    def get_item_types(cls):
        """
        Gives the available items in game

        Returns
        -------
            A list of strings which shows all available items in the game
        """
        print(
            f" the available item types in game are {cls.ITEM_TYPES[0]} and {cls.ITEM_TYPES[1]}"
        )

    @staticmethod
    def get_item_list():
        """
        Ensures only a singleton list of items 
        """
        if Item.__item_list == None:
            Item.__item_list = []
        return Item.__item_list


class Amulet(Item):
    def __init__(self, name):
        """
        Constructor class that initiates Amulet objects
        """
        super().__init__(name)

        print(f"{self.name} the amulet has been created")
        visuals.amulet_visual()

    def use_item(self, user_character):
        """
        User_character uses the amulet to increase attack_strength by magic_attack_strength

        Parameters
        ----------
        user_character
            The character who has equipped the amulet (Character)

        Returns
        -------
            The user character with its attack_strength increased by magic_attack_strength which 
            is a randomized value of either 1 or 2
        """
        if user_character.item == self.name:
            magic_attack_strength = randint(1, 2)
            user_character.attack_strength += magic_attack_strength
            print(
                f"{user_character.name} used {self.name} and now has {user_character.attack_strength} attack strength"
            )
        else:
            print(
                f"{user_character.name} does not have {self.name} equipped so cannot use it"
            )


class Armour(Item):
    def __init__(self, name):
        """
        Constructor class that initiates Armour objects
        """
        super().__init__(name)

        print(f"{self.name} the armour has been created")
        visuals.armour_visual()

    def use_item(self, user_character):
        """
        User character uses the armour to increase defence_strength by 1

        Paramaters
        ----------
        user_character
            The character who has equipped the armour (Character)

        Returns
        -------
            The user_character has its defence_strength increased by 1

        """
        if user_character.item == self.name:
            user_character.defence_strength += 1
            print(
                f"{user_character.name} used {self.name} and now has {user_character.defence_strength} defence strength"
            )
        else:
            print(
                f"{user_character.name} does not have {self.name} equipped so cannot use it"
            )


if __name__ == "__main__":

    # Making characters and items
    flame_goblin = Goblin("flame_goblin", "fire")
    fighter = Gladiator("fighter")
    basic_amulet = Amulet("basic_amulet")
    basic_armour = Armour("basic_armour")

    # Characters equip items
    flame_goblin.equip_item(basic_amulet)
    basic_amulet.use_item(flame_goblin)

    fighter.equip_item(basic_armour)
    basic_armour.use_item(fighter)

    # Fight begins
    flame_goblin.type_spell()  #  flame_goblin increases its stats
    fighter.attack(flame_goblin)
    flame_goblin.attack(fighter)
    fighter.berserk_attack(flame_goblin)
