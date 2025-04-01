from typing import Optional, cast

_true_set = {"yes", "true", "t", "y", "1"}
_false_set = {"no", "false", "f", "n", "0"}


def str2bool(value: str, raise_exc: bool = False) -> Optional[bool]:
    """
    Convert a string to a boolean value.

    Args:
        value (str): The string to convert.
        raise_exc (bool, optional): Whether to raise an exception if the string cannot be converted. Defaults to False.

    Returns:
        Optional[bool]: The converted boolean value, or None if the string cannot be converted and raise_exc is False.
    """
    if isinstance(value, str):
        value = value.lower()
        if value in _true_set:
            return True
        if value in _false_set:
            return False

    if raise_exc:
        raise ValueError('Expected "{}"'.format('", "'.join(_true_set | _false_set)))

    return None


def str2bool_exc(value: str) -> bool:
    """
    Convert a string to a boolean value, raising an exception if the string cannot be converted.

    Args:
        value (str): The string to convert.

    Returns:
        bool: The converted boolean value.
    """
    # This is guaranteed to return a bool with `raise_exc=True`
    return cast(bool, str2bool(value, raise_exc=True))
