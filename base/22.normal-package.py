from datetime import datetime
from collections import namedtuple

dt = datetime(2015, 4, 19, 8, 20)
print(dt)

Point = namedtuple('Point', ['x', 'x'])
p = Point(1, 2)
print(p.x)
