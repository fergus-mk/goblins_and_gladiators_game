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

Note there are three types of goblin available: fire, forest and water - each of which have unique abilities

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

## Using Gladiator Characters
---

## Equipping And Using Items
---

## Playing The Game
---
