class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    # добавлен декоратор property для предотвращения изменения "name" снаружи
    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f'книга "{self._name}". Автор: {self._author}'

    def __repr__(self):
        return f"{type(self).__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self):
        return f"Бумажная {super().__str__()}. Страниц: {self.pages}."


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = value

    def __str__(self):
        return f"Аудио {super().__str__()}. Продолжительность: {self.duration} ч."

if __name__ == '__main__':

    paper_book = PaperBook("Мастер и Маргарита", "Михаил Булгаков", 480)
    audio_book = AudioBook("Белые ночи", "Фёдор Достоевский", 2.3)
    print(paper_book)  # Вывод: Бумажная книга "Мастер и Маргарита". Автор: Михаил Булгаков. Страниц: 480.
    print(audio_book)  # Вывод: Аудио книга "Белые ночи". Автор: Фёдор Достоевский. Продолжительность: 2.3 ч.

    try:
        invalid_paper_book = PaperBook("Ошибка", "Автор", -100)
    except ValueError as e:
        print(e)  # Вывод ошибки: "Количество страниц должно быть положительным числом"
