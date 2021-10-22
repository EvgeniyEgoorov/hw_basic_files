from pprint import pprint

with open('recipes.txt', mode='r',  encoding='utf-8-sig') as file:
    cook_book = {}
    for dish in file:
        dish_name = dish.strip()
        ingredients_qty = int(file.readline().strip())
        ingredients = []
        for els in range(ingredients_qty):
            name, qty, measure = file.readline().split('|')
            ingredient = {'name': name.strip(), 'qty': int(qty), 'measure': measure.strip()}
            ingredients.append(ingredient)
        cook_book[dish_name] = ingredients
        file.readline()
    pprint(cook_book, sort_dicts=False)



