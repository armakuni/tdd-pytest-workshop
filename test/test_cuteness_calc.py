from unittest import mock

import company_db
from company_db.cute_animal import CuteAnimal
from company_db.cuteness_calc import AnimalTooCuteException

## Tests
def test_can_get_cuteness_value(cute_animal_beatrice):
    with mock.patch("company_db.cuteness_calc.cuteness_age_adjustment") as mocker:
        mocker.return_value = 25

        assert calculate_cuteness(cute_animal=cute_animal_beatrice) == 25


def test_can_handle_exception(cute_animal_beatrice):
    with mock.patch("company_db.cuteness_calc.cuteness_age_adjustment") as mocker:
        mocker.side_effect = AnimalTooCuteException()
        
        assert calculate_cuteness(cute_animal_beatrice) == "Animal too cute for calculator"


## Production code
def calculate_cuteness(cute_animal: CuteAnimal):
    try:
        return company_db.cuteness_calc.cuteness_age_adjustment(cute_animal)
    except AnimalTooCuteException:
        return "Animal too cute for calculator"