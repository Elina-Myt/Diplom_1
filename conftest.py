from unittest.mock import Mock
import pytest
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture(scope='function')
def burger():
    burger = Burger()

    mock_ingredient_1 = Mock()
    mock_ingredient_1.type = INGREDIENT_TYPE_FILLING
    mock_ingredient_1.name = 'Лист салата'
    mock_ingredient_1.price = 1000

    mock_ingredient_2 = Mock()
    mock_ingredient_2.type = INGREDIENT_TYPE_SAUCE
    mock_ingredient_2.name = 'Кечунез'
    mock_ingredient_2.price = 2000

    burger.add_ingredient(mock_ingredient_1)
    burger.add_ingredient(mock_ingredient_2)

    return burger

