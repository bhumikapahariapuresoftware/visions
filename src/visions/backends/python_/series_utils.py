import functools
from collections import Callable
from typing import Sequence, TypeVar

T = TypeVar("T")


def sequence_not_empty(fn: Callable) -> Callable:
    """Decorator to exclude empty series"""

    @functools.wraps(fn)
    def inner(sequence: Sequence, *args, **kwargs) -> bool:
        if not any(True for _ in sequence):
            return False

        return fn(sequence, *args, **kwargs)

    return inner


def sequence_handle_none(fn: Callable) -> Callable:
    """Decorator for nullable series"""

    @functools.wraps(fn)
    def inner(sequence: Sequence, *args, **kwargs) -> bool:
        sequence = tuple(filter(None, sequence))
        return fn(sequence, *args, **kwargs)

    return inner