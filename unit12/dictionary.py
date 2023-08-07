Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> lux
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> lux = {'health': 490, 'health': 800, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> lux['health']
800
>>> lux
{'health': 800, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
>>> x
{100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
>>> x = {[10, 20]: 100}
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x = {[10, 20]: 100}
TypeError: unhashable type: 'list'
>>> x = {{'a': 10}: 100}
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x = {{'a': 10}: 100}
TypeError: unhashable type: 'dict'
>>> x = {}
>>> x
{}
>>> y = dict()
>>> y
{}
>>> lux1 = dict(health = 490, mana = 334, melee = 550, armor = 18.72)
>>> lux1
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
>>> lux2
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
>>> lux3
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})
>>> lux4
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
