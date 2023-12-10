# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Car:
    def __init__(self, first_release: int, horsepower: int):
        """
        Создание и подготовка к классу "Машина"

        :first_release: Год начала выпуска
        :horsepower: Количество лошадиных сил

        Примеры:
        >>> car = Car(2014, 347) #инициализация экземляра класса
        """
        if not isinstance(first_release, (int)):
            raise TypeError("Год начала выпуска должен быть типа int")
        if first_release <= 0:
            raise ValueError("Год начала выпуска должен быть положительным числом")
        self.first_release = first_release

        if not isinstance(horsepower, (int)):
            raise TypeError("Количество лошадиных сил должно быть int")
        if horsepower < 0:
            raise ValueError("Количество лошадиных сил не может быть отрицательным числом")
        self.horsepower = horsepower

        def is_old_car(self) -> bool:
            """
            Функция, которая проверяет, новая ли машина по году выпуска

            :return: является ли машина новой

            Примеры:
            >>> car = Car(2014, 347)
            >>> car.is_old_car()
            """
            ...

        def is_powerful_car(self) -> bool:
            """
            Функция, которая проверяет, мощная ли машина по количеству лошадиных сил

            :return: является ли машина мощной

            Примеры:
            >>> car = Car(2014, 347)
            >>> car.is_powerful_car()
            """
            ...

class Dress:
    def __init__(self, material: str, size: int, color: str):
        """
        Создание и подготовка к классу "Платье"

        :material: Материао
        :size: Размер (европейский)
        :color: Цвет

        Примеры:
        >>> dress = Dress("трикотаж", 46, "белый") #инициализация экземляра класса
        """

        if not isinstance(size, (int)):
            raise TypeError("Размер платья должен быть типа int")
        if size <= 0:
            raise ValueError("Размер платья должен быть положительным числом")
        self.size = size

        def change_size(self, size: int) -> int:
            """
            Функция, которая меняет размер платья

            :param size: Размер платья

            Примеры:
            >>> dress = Dress("трикотаж", 46, "белый")
            >>> dress.change_size(44)
            """
            if not isinstance(size, (int)):
                raise TypeError("Размер платья должен быть типа int")
            if size <= 0:
                raise ValueError("Размер платья должен быть положительным числом")
            self.size = size
            ...

        def is_comfortable_dress(self) -> bool:
            """
            Функция, которая определяет, удобное ли платье

            :return: является ли платье удобным

            Примеры:
            >>> dress = Dress("трикотаж", 46, "белый")
            >>> dress.is_comfortable_dress()
            """
            ...
            if not isinstance(size, (int)):
                raise TypeError("Размер платья должен быть типа int")
            if size <= 0:
                raise ValueError("Размер платья должен быть положительным числом")
            self.size = size

class Photo:
    def __init__(self, size: int, format: str):
        """
        Создание и подготовка к классу "Фотография"

        :size: Размер фотографии (Мб)
        :format: Формат фотографии

        Примеры:
        >>> photo = Photo(3, "jpeg") #инициализация экземляра класса
        """
        if not isinstance(size, (int)):
            raise TypeError("Размер фотографии должен быть типа int")
        if size <= 0:
            raise ValueError("Размер фотографии должен быть положительным числом")
        self.size = size

        def compression_photo(self, size) -> int:
            """
            Функция, которая сжимает фотографию

            :param size: Размер фотографии
            Примеры:
            >>> photo = Photo(3, "jpeg")
            >>> photo.compression_photo(2)
            """
            if not isinstance(size, (int)):
                raise TypeError("Размер фотографии должен быть типа int")
            if size <= 0:
                raise ValueError("Размер фотографии должен быть положительным числом")
            self.size = size
            ...

        def change_format(self, format) -> int:
            """
            Функция, которая меняет формат фотографии

            param format: Формат фотографии

            Примеры:
            >>> photo = Photo(3, "jpeg")
            >>> photo.change_format("png")
            """
            ...
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
