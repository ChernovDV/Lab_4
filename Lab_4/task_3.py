import random


list = []
def get_unique_list_numbers():
# написать функцию для получения списка уникальных целых чисел
    for i in range(16):
        number = random.randint(-10, 10)
        list.append(number)
    return list
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
