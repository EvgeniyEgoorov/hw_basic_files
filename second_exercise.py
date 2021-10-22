from pprint import pprint

cook_book = {
    'Омлет': [
        {'name': 'Яйцо', 'qty': 2, 'measure': 'шт.'},
        {'name': 'Молоко', 'qty': 100, 'measure': 'мл'},
        {'name': 'Помидор', 'qty': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'name': 'Утка', 'qty': 1, 'measure': 'шт'},
        {'name': 'Вода', 'qty': 2, 'measure': 'л'},
        {'name': 'Мед', 'qty': 3, 'measure': 'ст.л'},
        {'name': 'Соевый соус', 'qty': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'name': 'Картофель', 'qty': 1, 'measure': 'кг'},
        {'name': 'Чеснок', 'qty': 3, 'measure': 'зубч'},
        {'name': 'Сыр гауда', 'qty': 100, 'measure': 'г'},
    ],
    'Фахитос': [
        {'name': 'Говядина', 'qty': 500, 'measure': 'г'},
        {'name': 'Перец сладкий', 'qty': 1, 'measure': 'шт'},
        {'name': 'Лаваш', 'qty': 2, 'measure': 'шт'},
        {'name': 'Винный уксус', 'qty': 1, 'measure': 'ст.л'},
        {'name': 'Помидор', 'qty': 2, 'measure': 'шт'}
    ]}


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient['qty'] *= person_count
            if ingredient['name'] not in shop_list.keys():
                shop_list[ingredient['name']] = {}
                shop_list[ingredient['name']]['qty'] = ingredient['qty']
                shop_list[ingredient['name']]['measure'] = ingredient['measure']
            else:
                shop_list[ingredient['name']]['qty'] += ingredient['qty']
    return shop_list


pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 5), sort_dicts=False)
