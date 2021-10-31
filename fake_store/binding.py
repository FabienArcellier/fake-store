import inspect
from typing import Type, Optional

BINDING = {}


def bind_class(name: str, klass: Type):
    assert inspect.isclass(klass), f"{klass} must be a class"

    BINDING[name] = klass


def binded_class(name: str) -> Optional[Type]:
    if name not in BINDING:
        return None

    return BINDING[name]
