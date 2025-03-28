"""
This module provides a utility function for loading a class using its fully qualified class string.

The `load_class` function allows you to dynamically import the required module and retrieve the class object based on
the provided fully qualified class string.

Example usage:
    load_class('ferris_fab_data_quality.views.dqcheck_view.DQChecksView')

"""


def load_class(name):
    """
    Load a class using its fully qualified class string.

    Args:
        name (str): The fully qualified class string, e.g., 'package.module.Class'.

    Returns:
        class: The loaded class object.

    Example:
        load_class('ferris_fab_data_quality.views.dqcheck_view.DQChecksView')

    """
    components = name.split(".")
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod
