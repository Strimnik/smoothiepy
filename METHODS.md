# Methods

Each easing class implements the following methods:

- **in_(t)**: Calculates the easing value at the start of the animation.
- **out(t)**: Calculates the easing value at the end of the animation.
- **in_out(t)**: Calculates the easing value in the middle of the animation.
- **out_in(t)**: Calculates the easing value by combining the start and end of the animation.

## `get_easing_class(easing_type)`

Gets the easing class corresponding to the provided type.

```python
def get_easing_class(easing_type):
    """
    Gets the easing class corresponding to the provided type.

    :param easing_type: The name of the easing type (e.g., 'Quad').
    :return: The corresponding easing class.
    """
```