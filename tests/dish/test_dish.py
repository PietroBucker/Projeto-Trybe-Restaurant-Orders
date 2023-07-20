from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest
from src.models.ingredient import Ingredient


# Req 2
def test_dish():
    cardapio1 = Dish("lasanha", 10)
    cardapio2 = Dish("lasanha", 10)
    cardapio3 = Dish("arroz", 10)
    assert cardapio1.name == "lasanha"
    assert cardapio1 == cardapio2
    assert cardapio1 != cardapio3
    assert str(cardapio1) == "Dish('lasanha', R$10.00)"
    assert hash(cardapio1) == hash(cardapio2)
    assert hash(cardapio1) != hash(cardapio3)

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("farinha", "10")
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("farinha", 0)

    cardapio1.add_ingredient_dependency(Ingredient("farinha"), 10)
    assert cardapio1.recipe.get(Ingredient("farinha")) == 10
    assert cardapio1.get_ingredients() == {Ingredient('farinha')}

    assert (
        str(cardapio1.get_restrictions()) == "{<Restriction.GLUTEN: 'GLUTEN'>}"
    )
    assert (
        str(cardapio1.get_restrictions())
        != "{<Restriction.GLUTEN: 'LACTOSE'>}"
    )
