# Usage

## Import the Library

To use `smoothiepy`, first import the module and then select the easing class you want to use.

```python
from smoothiepy import get_easing_class

# Select the easing class
Easing = get_easing_class('Quad')
easing = Easing()

# Use the easing function
t = 0.5  # A value between 0 and 1
print("In:", easing.in_(t))
print("Out:", easing.out(t))
print("In-Out:", easing.in_out(t))
print("Out-In:", easing.out_in(t))
```