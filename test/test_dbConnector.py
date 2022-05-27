from unittest import mock

import pytest

import company_db


@pytest.fixture
def cute_animals_list():
    return ["beatrice", "reginald", "bernard", "samantha"]


@pytest.fixture
def cute_animal_beatrice_dict():
    return {"name": "beatrice", "age": 10, "cuteness_level": 4000}


# Task 1
def test_get_cute_animals(cute_animals_list):
    with mock.patch("company_db.get_cute_animals") as mocker:
        mocker.return_value = cute_animals_list
        
        assert get_those_animals() == cute_animals_list


def get_those_animals():
    return company_db.get_cute_animals()


# Task 2
def test_get_cute_animal(cute_animal_beatrice, cute_animal_beatrice_dict):
    with mock.patch("company_db.get_cute_animal") as mocker:
        mocker.return_value = cute_animal_beatrice

        assert (
            get_animal_deets(cute_animal_name="beatrice") == cute_animal_beatrice_dict
        )


def get_animal_deets(cute_animal_name: str):
    return company_db.get_cute_animal(name=cute_animal_name).to_dict()
