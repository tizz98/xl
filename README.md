# xl
Create Excel formulas in python. The way some of the objects work was highly inspired
by Django's `Q` and `F` objects.

# Examples
_All examples in `examples/` folder_

### Basic
```python
from xl import *

print(IF(Cell('a', 2) > Cell('a', 1), Cell('a', 3), Cell('a', 5)))
print(IF(Cell('a', 2).gte(Cell('a', 1)), Cell('a', 3), Cell('a', 5)))
print(IF(Cell('a', 2) == Cell('a', 1), Cell('a', 3), Cell('a', 5)))
print(IF(Cell('a', 2) != Cell('a', 1), Cell('a', 3), Cell('a', 5)))
print(IF(Cell('a', 2) < Cell('a', 1), Cell('a', 3), Cell('a', 5)))
print(IF(Cell('a', 2).lte(Cell('a', 1)), Cell('a', 3), Cell('a', 5)))
print(IF(Cell('a', 2) & Cell('a', 1), Cell('a', 3), Cell('a', 5)))
print(IF(Cell('a', 2) | Cell('a', 1), Cell('a', 3), Cell('a', 5)))

print(Cell('a', 2) + Cell('a', 3))
print(Cell('a', 2) - Cell('a', 3))
print(Cell('a', 2) * Cell('a', 3))
print(Cell('a', 2) / Cell('a', 3))

print(IFS(
    Cell('a', 2, 'Sheet1') > Cell('a', 1, 'Sheet2'), Cell('a', 3),
    Cell('a', 2) == Cell('a', 1), Cell('a', 5)
))

print(IFERROR(Cell('a', 2) / Cell('a', 4), 0))

print(IF(
    Cell('a', 2),
    IF(Cell('a', 3) > Cell('b', 3), Cell('c', 3), Cell('d', 3)),
    Cell('e', 3)
))

print(SUM(Range(Cell('c', sheet='Sheet1'), Cell('c'))))
```
