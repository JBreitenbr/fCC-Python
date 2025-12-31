"""
Build an RPG Character
In this lab you will practice the basics of Python by building a small app that creates a character for an RPG adventure.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should have a function named create_character.
The function should accept, in order, a character name followed by three stats: strength, intelligence, and charisma.
The character name should be validated:
If the character name is not a string, the function should return The character name should be a string.
If the character name is an empty string, the function should return The character should have a name.
If the character name is longer than 10 characters, the function should return The character name is too long.
If the character name contains spaces, the function should return The character name should not contain spaces.
The stats should also be validated:
If one or more stats are not integers, the function should return All stats should be integers.
If one or more stats are less than 1, the function should return All stats should be no less than 1.
If one or more stats are more than 4, the function should return All stats should be no more than 4.
If the sum of all stats is different than 7, the function should return The character should start with 7 points.
If all values pass the verification, the function should return a string with four lines:
the first line should contain the character name
lines 2-4 should start with the stat abbreviation, STR, INT or CHA (in this order), then a space, and then a number of full dots (●) equal to the value of the stat, and a number of empty dots (○) to reach 10. Example: if the value of strength is 3 there must be 3 full dots followed by 7 empty dots. The dots are given in the editor.
Here's the string that should be returned by create_character('ren', 4, 2, 1):

Example Code
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
NOTE: while str and int are common abbreviations for the stats, remember that those are reserved keywords in Python and should not be used as variable names.
"""

full_dot = '●'
empty_dot = '○'

def create_character(cName, cStr, cInt, cCha):
    if not isinstance(cName, str):
        return 'The character name should be a string'
    if len(cName) > 10:
        return 'The character name is too long'
    if ' ' in cName:
        return 'The character name should not contain spaces'
    if not isinstance(cStr, int) or not isinstance(cInt, int) or not isinstance(cCha, int):
        return 'All stats should be integers'
    if cStr < 1 or cInt < 1 or cCha < 1:
        return 'All stats should be no less than 1'
    if cStr > 4 or cInt > 4 or cCha > 4:
        return 'All stats should be no more than 4'
    if (cStr+cInt+cCha) != 7:
        return 'The character should start with 7 points'
    return f"{cName}\nSTR {full_dot*cStr}{empty_dot*(10-cStr)}\nINT {full_dot*cInt}{empty_dot*(10-cInt)}\nCHA {full_dot*cCha}{empty_dot*(10-cCha)}"
print(create_character("Julia", 4, 2, 1))
