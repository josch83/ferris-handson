"""
This module provides a utility function for converting a string representation of a dictionary to a dictionary object.

The `str_to_dict` function parses the input string using the `json.loads` function and returns the resulting
dictionary.
If parsing fails, an empty dictionary is returned.

"""

import json


def str_to_dict(strn):
    """
    Converts a string representation of a dictionary to a dictionary object.

    Args:
        strn (str): The string representation of a dictionary.

    Returns:
        dict: The dictionary object parsed from the input string.

    Note:
        If parsing fails, an empty dictionary is returned.

    """
    try:
        return json.loads(strn)
    except Exception as exception:
        print(f"Exception when trying to convert string to dictionary: {exception}")
        return {}
