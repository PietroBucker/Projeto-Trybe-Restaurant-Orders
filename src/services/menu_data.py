# Req 3
import csv
from models.dish import Dish
from models.ingredient import Ingredient

DATA_PATH = "tests/mocks/menu_base_data.csv"


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.path = source_path
        self.file_open()

    def __len__(self):
        return len(self.dishes)

    def file_open(self):
        with open(self.path, encoding="utf-8") as file:
            menu_itens = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = menu_itens

        nomes_pratos = set()
        for line in data:
            nomes_pratos.add((line[0], line[1]))

        for nome, price in nomes_pratos:
            new_dish = Dish(nome, float(price))
            for line in data:
                if line[0] == nome:
                    new_dish.add_ingredient_dependency(
                        Ingredient(line[2]), int(line[3])
                    )
            self.dishes.add(new_dish)


teste = MenuData(DATA_PATH)
teste.file_open()
teste2 = list(teste.dishes)
print(teste2[0].get_ingredients())
print(teste2[1].get_ingredients())
