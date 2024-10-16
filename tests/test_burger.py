import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE

class TestBurger:

    def test_set_bun(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1 and burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, burger):
        removed_ingredient = burger.ingredients[0]
        burger.remove_ingredient(0)

        assert removed_ingredient not in burger.ingredients

    def test_move_ingredient(self, burger):
        moved_ingredient = burger.ingredients[1]
        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == moved_ingredient

    @pytest.mark.parametrize('bun_price, ingredient_1_price, ingredient_2_price, expected_result', [
        [0, 0, 0, 0],
        [1000.0, 0, 0, 2000.0],
        [3000.0, 3000, 2000, 11000.0]
    ])
    def test_get_price(self, bun_price, ingredient_1_price, ingredient_2_price, expected_result):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = ingredient_1_price
        burger.add_ingredient(mock_ingredient_1)

        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_price.return_value = ingredient_2_price
        burger.add_ingredient(mock_ingredient_2)

        burger_price = burger.get_price()

        assert burger_price == expected_result

    def test_get_receipt(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Космическая булка'
        mock_bun.get_price.return_value = 6000

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = 'Кечунез'
        mock_ingredient.get_price.return_value = 3000

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        result_receipt = [
            '(==== Космическая булка ====)',
            '= sauce Кечунез =',
            '(==== Космическая булка ====)\n',
            'Price: 15000'
        ]

        assert str(burger.get_receipt()) == '\n'.join(result_receipt)