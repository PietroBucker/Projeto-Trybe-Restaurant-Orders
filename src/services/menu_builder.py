from typing import Dict, List

# from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        # self.inventory = InventoryMapping(inventory_path)

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
            # print(prato.name)
            # print(restriction in str(prato.get_restrictions()))
            if restriction in str(prato.get_restrictions()):
                list.append(
                    {
                        "dish_name": prato.name,
                        "ingredients": [
                            ingredient.name
                            for ingredient in list(prato.get_ingredients())
                        ],
                        
                    }
                )


teste = MenuBuilder(DATA_PATH, INVENTORY_PATH)
teste.get_main_menu("Restriction.ANIMAL_MEAT")
