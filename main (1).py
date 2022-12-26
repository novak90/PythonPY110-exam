import json
import faker
from itertools import count
from conf import MODEL
from random import randint, uniform
fake = faker.Faker("ru")  # импортировали все необходимые библиотеки


def gen_counter_for_random_books(counter=1):
    for current_number in count(counter):
        yield current_number
    return


def title_for_random_books() -> str:  # Функция для вывода произвольной строки названия книги из файла "Books.txt".
    # :return: строка str с названием книги;

    input_file = "Books.txt"
    r = open(input_file, "r", encoding="utf-8")
    for i,  line in enumerate(r):
        line = line.replace("\n", "")
        if i >= randint(0, 8):
            return line


def year_for_random_books():
    return randint(0, 2020)  # функция возвращает год в промежутке от 0 до 2020


def pages_for_random_books():
    return randint(10, 1000)  # случайное количество страниц


def isbn13_for_random_books() -> str:
    return fake.isbn13()    # функция возвращает случайный набор чисел по формату ISBN13


def rate_of_random_books():
    return uniform(1, 10)


def author_of_random_books() -> list:  # функция возвращает список в котором содержится от 1 до 3 имен и фамилий,
    # рандомных мужских и женских
    output_names = []
    for i in range(randint(1, 3)):
        if i == randint(1, 3):
            output_names.append(fake.first_name_male() + " " + fake.last_name_male())
        else:
            output_names.append(fake.first_name_female() + " " + fake.last_name_female())
        return output_names


def price_of_random_books():  # возвращает произвольную стоимость книги в промежутке от 1 до 100
    return str(uniform(1, 100))


def json_file_for_random_books(obj_data: dict, output_file: str) -> None:  # Функция для записи сгенерированных элементов в файл output_file типа json. Файл может быть создан с нуля.
    # :param obj_data: словарь сгенерированных данных, который необходимо записать;
    # :param output_file: название файла, в которое предстоит произвести запись;
    # :return: None
    
    
    with open(output_file, "a", encoding="utf-8") as f:
        json.dump(obj_data, f, indent=4, ensure_ascii=False)


def json_cleaner(output_file: str) -> None:  # Функция для очистки файла output_file типа json
    open(output_file, "w")


def main() -> None:
    """
    Функция для генерации 100 различных массивов данных типа dict, содержащих: модель, счётчик, поля.
    В словаре "поля" прописаны: название книги, год, количество страниц, номер ISBN13, рейтинг, цена, автор.
    Использует функцию clear_json для очистки файла json и to_json_file для записи в файл json.
    :return: None
    """
    output_plug = "output.json"
    json_cleaner(output_plug)
    pk = gen_counter_for_random_books()
    fields = ({"title": title_for_random_books(),
               "year": year_for_random_books(),
               "pages": pages_for_random_books(),
               "isbn13": isbn13_for_random_books(),
               "rating": rate_of_random_books(),
               "price": price_of_random_books(),
               "author": author_of_random_books()} for a in count())
    data = ({"model": MODEL, "pk": next(pk), "fields": next(fields)} for b in count())
    for c in range(100):
        json_file_for_random_books(next(data), output_plug)


if __name__ == '__main__':
    main()
