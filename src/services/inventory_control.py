from csv import DictReader, DictWriter
from typing import Dict

from models.dish import Recipe
from models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


def write_csv_inventory(
    new_inventory, inventory_file_path=BASE_INVENTORY
) -> None:
    cabecalho = ["ingredient", "initial_amount"]
    with open(inventory_file_path, mode="w", encoding="utf-8") as file:
        writer = DictWriter(file, fieldnames=cabecalho)
        writer.writeheader()

        for item in new_inventory:
            new_dict = {
                "ingredient": item.name,
                "initial_amount": new_inventory[item],
            }
            writer.writerow(new_dict)

    return


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe) -> bool:
        # print(recipe[Ingredient('farinha')])
        for item in recipe:
            if (
                item not in self.inventory
                or recipe[item] > self.inventory[item]
            ):
                return False
        return True

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        if self.check_recipe_availability(recipe):
            for item in recipe:
                self.inventory[item] -= recipe[item]
            # print(self.inventory)
            write_csv_inventory(self.inventory)
        else:
            raise ValueError("ValueError")
