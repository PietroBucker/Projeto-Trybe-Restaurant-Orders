teste = MenuData(DATA_PATH)
teste.file_open()
teste2 = list(teste.dishes)
print(teste2)
print(list(teste2[0].get_ingredients()))