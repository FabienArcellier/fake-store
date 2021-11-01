## Fake Store

[![ci](https://github.com/FabienArcellier/fake-store/actions/workflows/ci.yml/badge.svg)](https://github.com/FabienArcellier/fake-store/actions/workflows/ci.yml)

With fake-store, the implementation of a hexagonal architecture in python whose repositories are testable becomes
very simple.

This library is able to make hydrated entities from yaml files. It will let use them directly.
This is the ideal library for building your fake server that replaces your database in automatic tests.

```python
class FakePetRepository:

    def __init__(self):
        self._store: List[Pet] = fake_store.load_collection(Pet, "pet.yml")

    def store(self, pet: Pet):
        self._store.append(pet)

    ...
```

The librarie takes care of :

* loading nested object inside each other
* converting objects to their native python type
* take controle of objects generation through a factory
* works well with ``dataclass`` and ``attrs``
* implement a share memory store and resettable memory store to share datasets between repositories

## Getting started

```
pip install fake-store
```

## The latest version

You can find the latest version to ...

```bash
git clone https://github.com/FabienArcellier/fake-store.git
```

## Usage

### Binding _class in definition with real python class

You can run the application with the following command

```python
import fake_store
from myapp.domain.entity.pet import Pet

fake_store.bind_class(Pet.__name__, Pet)
```

Any objects that contains `_class: Pet` in definition will be instanciated as `Pet`

```yaml
- __class: Pet
  name: "Ronny"
  status: available

- __class: Pet
  name: "Crane"
  status: unavailable
```

The class Pet has to defined it's ``__init__`` method with the 2 keyword arguments. If an argument is missing or
doesn't exist in the construct, it will raise an error

```python
class Pet:

    def __init__(self, name: str, status: str):
        pass
```

look at [examples/nested_fake_store.py](examples/nested_fake_store.py)

### use a factory method instead of __init__ method

see [examples/factory_fake_store.py](examples/factory_fake_store.py)

### use a memory store to share the same data between several repository

see [examples/memory_store.py](examples/memory_store.py)

### use a resettable memory store to share the same data between several repository on automatic test

Data loading can become slower and slower over time. If it is played between each test, it adds
1s of overhead on every test. In a CI or on the development workstation, it is interesting to avoid
this loading time.

The ``ResettableStore`` class allows between each test to restore the content of the store to its original state in one step
negligible with the call to `reset_store`.

see [examples/resettable_store.py](examples/resettable_store.py)

## Developper guideline

```
activate                       activate the virtualenv associate with this project
coverage                       output the code coverage in htmlcov/index.html
help                           provides cli help for this makefile (default)
install_requirements_dev       install pip requirements for development
install_requirements           install pip requirements based on requirements.txt
lint                           run pylint
tests                          run automatic tests
tests_units                    run only unit tests
twine                          publish on pypi
update_requirements            update the project dependencies based on setup.py declaration
```

### Install development environment

Use make to instanciate a python virtual environment in ./venv and install the
python dependencies.

```bash
make install_requirements_dev
```

### Install production environment

```bash
make install_requirements
```

### Initiate or update the library requirements

If you want to initiate or update all the requirements `install_requires` declared in `setup.py`
and freeze a new `Pipfile.lock`, use this command

```bash
make update_requirements
```

### Activate the python environment

When you setup the requirements, a `venv` directory on python 3 is created.
To activate the venv, you have to execute :

```bash
make venv
source venv/bin/activate
```

### Run the linter and the unit tests

Before commit or send a pull request, you have to execute `pylint` to check the syntax
of your code and run the unit tests to validate the behavior.

```bash
make lint
make tests
```

## Contributors

* Fabien Arcellier

## License

MIT License

Copyright (c) 2018 Fabien Arcellier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
