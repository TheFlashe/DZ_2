# Задание №1


# def book_of_recep():
#     cook_book = {}
#     with open('text.txt', 'r', encoding='UTF-8') as file:
#         for dish in file:
#             cook_book[dish.strip()] = []
#             for item in range(int(file.readline())):
#                 items = list(file.readline().strip().split(' | '))
#                 cook_book[dish.strip()].append({'ingredient_name': items[0], 'quantity': items[1], 'measure': items[2]})
#             file.readline()
#         return cook_book
#
#     # get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
#     # {
#     #   'Картофель': {'measure': 'кг', 'quantity': 2},
#     #   'Молоко': {'measure': 'мл', 'quantity': 200},
#     #   'Помидор': {'measure': 'шт', 'quantity': 4},
#     #   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#     #   'Яйцо': {'measure': 'шт', 'quantity': 4},
#     #   'Чеснок': {'measure': 'зубч', 'quantity': 6}
#     # }
#
#
# # Задание №2
# def get_shop_list_by_dishes(dishes, person_count):
#     ingredients_list = []
#     for dish in dishes:
#         if dish in dishes:
#             ingredients_list += book_of_recep().get(dish)
#     # print(ingredients_list)
#
#     new_dict = {}
#     for ingri in ingredients_list:
#         main_ingri = ingri.pop('ingredient_name')
#         if main_ingri not in new_dict.keys():
#             new_dict[main_ingri] = ingri
#         else:
#             # print(new_dict[main_ingri]['quantity'])
#             new_dict[main_ingri]['quantity'] = int(new_dict[main_ingri]['quantity']) + int(ingri['quantity'])
#     print(f'Список ингридиентов для {person_count} персон: ')
#     for ke, vals in new_dict.items():
#         print(f"{ke} {int(vals['quantity']) * person_count} {vals['measure']}")  # кол-во томатов подправаил в блюде
#         # print(new_dict)
# #
# #
# get_shop_list_by_dishes(['Омлет', 'Омлет'], 2) #Фахитос

# Задание №3


def count_lines_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(1 for line in file)  # считаю количество строк


def get_file_line_counts(file_names):
    file_lin = {}
    for file_name in file_names:
        line_count = count_lines_in_file(file_name)
        file_lin[file_name] = line_count
    return file_lin


def write_sorted_files(file_lin, output_file):
    sorted_files = sorted(file_lin.items(), key=lambda item: item[1])
    with open(output_file, 'w', encoding='utf-8') as output:
        for file_name, count in sorted_files:
            output.write(f"{file_name}\n{count}\n")
            with open(file_name, 'r', encoding='utf-8') as f:
                content = f.read()
                output.write(content + '\n')


def main(file_names, output_file):
    file_lin = get_file_line_counts(file_names)
    write_sorted_files(file_lin, output_file)


file_names = ['1.txt', '2.txt', '3.txt']
output_file = 'union.txt'
main(file_names, output_file)
