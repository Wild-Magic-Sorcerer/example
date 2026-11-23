#!/usr/bin/env python
from enum import Enum

DEFAULT_VALUE_ZERO = 0
DEFAULT_MINIMAL_AGE_FOR_DRINKING = 18
DEFAULT_MAXIMUM_SPEED = 100
DEFAULT_GREETINGS = 'Привет'

class Constants(Enum):
    value_zero: int = DEFAULT_VALUE_ZERO
    minimal_age_for_drinking: int = DEFAULT_MINIMAL_AGE_FOR_DRINKING
    maximum_speed: int = DEFAULT_MAXIMUM_SPEED
    greetings: str = DEFAULT_GREETINGS


if __name__ == '__main__':
    pass