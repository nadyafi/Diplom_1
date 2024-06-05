import pytest
from burger import Burger
from ingredient import Ingredient
from bun import Bun
from database import Database
from ingredient_types import *
from unittest.mock import Mock


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', 200.0)


@pytest.fixture
def bun():
    return Bun("black bun", 100.0)


@pytest.fixture
def database():
    return Database()


@pytest.fixture
def sauce():
    mock_sauce = Mock()
    mock_sauce.get_price.return_value = 50.0
    mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_sauce.get_name.return_value = 'Ketchup'
    return mock_sauce


@pytest.fixture
def filling():
    mock_filling = Mock()
    mock_filling.get_price.return_value = 1000.0
    mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock_filling.get_name.return_value = 'Beef'
    return mock_filling


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_price.return_value = 100.0
    mock_bun.get_name.return_value = 'Bun'
    return mock_bun
