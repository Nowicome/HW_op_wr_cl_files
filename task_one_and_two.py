from pprint import pprint


def order(menu):
    order_list = []
    while True:
        print(f"список доступных блюд: {', '.join(sorted(cook_book.keys()))}")
        print(f"Блюда в текущем заказе: {', '.join(sorted(order_list))}")
        add = input("Введите название блюда, чтобы добавить его к заказу или нажмите энтер для продолжения: ")
        if not add:
            print()
            break
        elif add in cook_book.keys():
            order_list.append(add)
            print()
        else:
            print("В НАШЕМ МЕНЮ НЕТ ТАКОГО БЛЮДА")
            print()
    while True:
        qty = int(input("Введите количество персон: "))
        if qty:
            print()
            break
    order_list = ing_count(menu, order_list, qty)
    return order_list


def ing_count(menu, dish_list, persons):
    dishes = {}
    for i in dish_list:
        for j in menu[i]:
            if j["ingredient"] in dishes.keys():
                dishes[j["ingredient"]] =\
                    {"measure": j["measure"],
                     "quantity": dishes[j["ingredient"]].get("quantity") + j.get("quantity") * persons}
            else:
                dishes[j["ingredient"]] = {"measure": j["measure"], "quantity": j.get("quantity") * persons}
    return dishes


if __name__ == "__main__":
    with open("recipes.txt", encoding="utf-8") as rec:
        cook_book = {}
        for dish_name in rec:
            dish = dish_name.strip()
            rec.readline()
            content = []
            line = rec.readline()
            while " | " in line:
                ingredient, quantity, measure = line.strip().split(" | ")
                content.append({
                    "ingredient": ingredient,
                    "quantity": int(quantity),
                    "measure": measure
                })
                line = rec.readline()
            cook_book[dish] = content
    # pprint(cook_book, sort_dicts=False)
    pprint(order(cook_book))
