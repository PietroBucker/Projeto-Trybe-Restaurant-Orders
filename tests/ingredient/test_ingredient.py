from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("farinha")
    ingredient3 = Ingredient("ovo")
    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3
    assert str(ingredient1) == "Ingredient('farinha')"
    assert hash(ingredient1) == hash(ingredient2)
    assert hash(ingredient1) != hash(ingredient3)
    assert str(ingredient1.restrictions) == "{<Restriction.GLUTEN: 'GLUTEN'>}"
    assert ingredient1.name == "farinha"
