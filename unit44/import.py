Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> math.pi
3.141592653589793
>>> math.sqrt(4.0)
2.0
>>> math.sqrt(2.0)
1.4142135623730951
>>> import math as m
>>> m.sqrt(4.0)
2.0
>>> m.sqrt(2.0)
1.4142135623730951
>>> from math import pi
>>> pi
3.141592653589793
>>> from math import sqrt
>>> sqrt(4.0)
2.0
>>> sqrt(2.0)
1.4142135623730951
>>> from math import pi, sqrt
>>> pi
3.141592653589793
>>> sqrt(4.0)
2.0
>>> sqrt(2.0)
1.4142135623730951
>>> from math import *
>>> pi
3.141592653589793
>>> sqrt(4.0)
2.0
>>> sqrt(2.0)
1.4142135623730951
>>> from math import sqrt as s
>>> s(4.0)
2.0
>>> s(2.0)
1.4142135623730951
from math import pi as p, sqrt as s
p
3.141592653589793
s(4.0)
2.0
s(2.0)
1.4142135623730951
import math
del math
import importlib
import math
importlib.reload(math)
<module 'math' (built-in)>
