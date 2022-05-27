import pytest

from company_db.cute_animal import CuteAnimal


@pytest.fixture
def example_dict():
    return {"name": "Steven", "age": 6, "cuteness_level": 18000}


@pytest.fixture
def cute_animal_beatrice():
    return CuteAnimal(name="beatrice", age=10, cuteness_level=4000)
