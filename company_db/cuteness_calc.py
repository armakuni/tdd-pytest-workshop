import random

from cute_animal import CuteAnimal


class AnimalTooCuteException(Exception):
    pass


def cuteness_age_adjustment(animal: CuteAnimal) -> float:
    r = random.random()
    if r < 0.2:
        raise AnimalTooCuteException()
    else:
        return animal.cuteness_level / animal.age
