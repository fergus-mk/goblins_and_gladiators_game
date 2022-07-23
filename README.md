# Overview
---

Goblins & Gladiators is a two player game where players create characters who fight each other. Players can create either goblins or gladiators both of which have unique strengths and abilities and equip their chosen character with items to increase its strength

# Instructions
---

## Initial Set-Up
--- 
The project uses packages contained in the goblin.yml file. Users should use the following command line 
command to initiate the environment:

`conda env create -f goblin.yml`

To initiate the game users should navigate to the goblins_and_gladiators folder. Once in the folder users should initate a Python shell with the command:

`python`

Next, users should import the characters file to start creating characters:

`import characters`

## Creating Characters
---
To create a goblin character players should adapt the following command:

`new_character = characters.Goblin('new_character_name', 'fire')`

The player is specifiyiing both the goblins name and type. Note there are three types of goblin available: 'fire', 'forest' and 'water' - each of which have unique abilities

Gladiator characers do not have a type. Players can create them by adapting the following command:

`new_character = characters.Gladiator('new_character_name')`

## Commands Useable For All Characters
---
Some commands can be used by all characters:

### Character Details

`new_character.character_details()`

Brings up key details of the character such as its name, hp, attack strength and defence strength.
Hp describes how much health a character has, when a characters health runs out it has lost the game. Attack strength describes how good it is at attacking and defence strength describes how resiliant it is to attacks from opponents 

### Attack

`new_character.attack(opponent_character)`

Is used to attack opponents. Attacks can do variable amounts of damage contingent on the attacking characters attack strength, the defending characters defence strength and a random element. Additionally there is a chance that attacks miss and do no damage

## Using Goblin Characters
---

Goblin characters have unique abilities:

### Healing Spell

`new_character.healing_spell()`

Heals the character by up to 2 hp

### Type Spell

`new_character.type_spell()`

This has a different effect depending on the type of goblin:
- For fire goblin it increases attack strength by 1
- For forest goblin it increased defence strength by 1
- For water goblin it increases hp (and max hp) by 2

### Get Goblin Types

`new_character.get_goblin_types()`

Returns a list of the possible types of goblin

## Using Gladiator Characters
---

Gladiator characters also have unique abilities:

### Berserk Attack

`new_character.berserk_attack(opponent_character)`

Like regular attack it is used to attack opponents. Berserk attacks can do variable amounts of damage contingent on the attacking characters attack strength, the defending characters defence strength and a random element. Additionally there is a chance that attacks miss and do no damage. The berserk attack is extra strong and does increased damage compared to a regular attack. It also damages the gladiator character who performs the attack through recoil

## Equipping And Using Items
---

Note all characters can equip and use items, however as this requires additional explanation this section of the instructions was especially created.

### Creating Items

First an item must be created by the player. Items can either be of amulet type, created with:

`new_amulet = characters.Amulet('new_amulet')`

Or of armour type, created with:

`new_armour = characters.Armour('new_armour')`

### Equipping Items

Characters must equip an item before using it, this is done with the following command:

`new_character.equip(new_item)`

### Using Items

Characters can use an item with the command:

`new_item.use_item(new_character)`

An amulet item increases the users attack strength by a random amount

An armour item increases the users defence strength by 1

## Playing The Game
---
Playing the game is simple. Each player needs to create a character and equip it with an item if desired.Players take it in turns to perform a single action i.e. attack, healing_spell, use_amulet etc. In this manner the two characters fight. When a character runs out of hp it is defeated and the other player has won. Note equipping any items should be done before the fight begins and therefore doesn't use an action