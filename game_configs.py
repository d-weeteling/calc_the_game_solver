from functions import *

configs = [
    # Level 0:
    {
        "value_start": 0,
        "value_wanted": 2,
        "rounds_total": 2,
        "ops": { "add1": get_add_N(1) }
    },
    # Level 1:
    {
        "value_start": -1,
        "value_wanted": -81,
        "rounds_total": 1,
        "ops": {
            "[8..]": get_left_insert_N(8),
        }
    },
    # Level 2:
    {
        "value_start": 1,
        "value_wanted": 7,
        "rounds_total": 3,
        "ops": {
            " +4": get_add_N(4),
            " -2": get_add_N(-2)
        }
    }
]