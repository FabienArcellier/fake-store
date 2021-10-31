import copy
import io
import os
from datetime import datetime
from typing import TypeVar, List, Type, Union, Any

import yaml
from yaml import FullLoader

from fake_store.binding import binded_class

KLASS = TypeVar('KLASS')


def load(klass: Type[KLASS], file_path: str) -> List[KLASS]:
    file_path = os.path.realpath(file_path)
    if not os.path.isfile(file_path):
        raise OSError(f"{file_path} does not exists")

    with io.open(file_path, 'r', encoding="utf8") as stream:
        content = yaml.load(stream, Loader=FullLoader)
        return load_from_list(klass, content)


def load_from_list(klass: Type[KLASS], content: Union[dict, list]) -> List[KLASS]:  # pylint: disable=unused-argument
    store = copy.deepcopy(content)
    if not isinstance(content, list):
        raise ValueError("the content to decode should be a list to be converted in a list of object")

    for i, elt in enumerate(store):
        store[i] = _transform(elt)

    return store


def _transform(entity: Union[dict, list, int, float, str, datetime]) -> Any:
    if isinstance(entity, list):
        for i, attribute in entity:
            entity[i] = _transform(attribute)
    elif isinstance(entity, dict):
        for key, attribute in entity.items():
            if not key.startswith("__"): # ignore attributes that begins with __{var}
                entity[key] = _transform(attribute)

        if "__class" in entity:
            klass_id = entity["__class"]
            del entity["__class"]
            klass = binded_class(klass_id)
            if klass is None:
                raise RuntimeError(f"{klass_id} does not exist in binding. You should bind_class( ) for it")

            if "__factory" in entity:
                factory_name = entity["__factory"]
                del entity["__factory"]

                if not hasattr(klass, factory_name):
                    raise RuntimeError(f"factory method {factory_name} is missing in {klass}")

                factory = getattr(klass, factory_name)
                entity = factory(**entity)
            else:
                entity = klass(**entity)

    return entity
