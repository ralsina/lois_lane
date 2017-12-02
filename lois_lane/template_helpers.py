"""This module contains helpers for the templates.

Just create a function and expose it via the helpers dictionary.
"""


def title(text, level=0):
    """Given a title, format it as a title/subtitle/etc."""
    return '\n' + text + '\n' + '=-~_#%^' [level] * len(text) + '\n\n'


helpers = {
    '_title': title,
}
