Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> lux['health']
490
>>> lux['armor']
18.72
>>> lux['health'] = 2037
>>> lux['mana'] = 1184
>>> lux
{'health': 2037, 'mana': 1184, 'melee': 550, 'armor': 18.72}
>>> lux['mana_regen'] = 3.28
>>> lux
{'health': 2037, 'mana': 1184, 'melee': 550, 'armor': 18.72, 'mana_regen': 3.28}
>>> lux['attack_speed']
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    lux['attack_speed']
KeyError: 'attack_speed'
>>> 'health' in lux
True
>>> 'attack_speed' in lux
False
>>> 'attack_speed' not in lux
True
>>> 'health' not in lux
False
>>> len(lux)
5
>>> len({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})
4
