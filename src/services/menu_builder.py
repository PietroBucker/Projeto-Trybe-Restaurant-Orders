from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData
from models.ingredient import Ingredient, Restriction

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        lista_dishes = list(self.menu_data.dishes)
        new_list = list()
        for prato in lista_dishes:
            if not restriction or restriction not in prato.get_restrictions():
                new_list.append(
                    {
                        "dish_name": prato.name,
                        "ingredients": [
                            ingredient
                            for ingredient in list(prato.get_ingredients())
                        ],
                        "price": prato.price,
                        "restrictions": [
                            pratos
                            for pratos in list(prato.get_restrictions())
                        ],
                    }
                )
        teste = sorted(new_list, key=lambda new_list: new_list["dish_name"])
        return teste


# teste = MenuBuilder(DATA_PATH, INVENTORY_PATH)
# print(teste.get_main_menu(Restriction.ANIMAL_MEAT))
