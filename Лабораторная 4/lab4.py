class SocialMedia:
    def __init__(self, time: int, friends: int, nickname: str):
        """
        Создание и подготовка к классу "Социальные сети"

        :time: Продолжительность пользования социальной сетью (кол-во дней)
        :friends: Количество друзей в социальной сети
        :nickname: Никнейм аккаунта

        Примеры:
        >>> social_media = SocialMedia(730, 102, "black_cat")
        """

        if not isinstance(time, (int)):
            raise TypeError("Продолжительность пользования социальной сетью должна быть типа int")
        if time <= 0:
            raise ValueError("Продолжительность пользования социальной сетью должна быть положительным числом")
        self.time = time

        if not isinstance(friends, (int)):
            raise TypeError("Количество друзей в соципльной сети должно быть int")
        if friends < 0:
            raise ValueError("Количество друзей в соципльной сети не может быть отрицательным числом")
        self.friends = friends

        self.nickname = nickname

    def __str__(self) -> str:
        return f'Родительский класс "Социальные сети".'

    def __repr__(self) -> str:
        return f"{type(self).__name__}(time={self.time}, friends={self.friends}, nickname='{self.nickname}')"

    def is_user_registered(self) -> bool:
        """
        Функция, которая проверяет, зарегистрирован ли пользователь

        :return: зарегистрирован ли пользователь

        Примеры:
        >>> user = SocialMedia(100, 50, "nickname")
        >>> user.is_user_registered()
        """
        ...

    def change_friends(self) -> int:
        """
        Функция, которая добавляет другого пользователя в друзья

        :friend: пользователь, которого добавляют

        Примеры:
        >>> friends = SocialMedia(1,0, "nickname")
        >>> friends.change_friends()
        """
        return self.friends + 1
class VK(SocialMedia):
    def __str__(self) -> str:
        return f'Дочерний класс "ВКонтакте".'

    def send_message(self, nickname: str) -> str:
        """
               Функция, которая отправляет сообщение другому пользователю социальной сети

               :nickname: Никнейм пользователя-адресата

               Примеры:
               >>> message = VK(365, 120, "nickname1")
               >>> message.send_message("nickname2")
               """

        return input("Напишите ваше сообщение...\n")

    def change_friends(self) -> int:
        """
        Функция, которая удаляет другого пользователя из друзей

        :friend: пользователь, которого добавляют

        Примеры:
        >>> friends = SocialMedia(1,1, "nickname")
        >>> friends.change_friends()
        """
        return self.friends - 1

if __name__ == "__main__":
    user_ = SocialMedia(100, 20, "person")
    print(str(user_)) #Вывод: Родительский класс "Социальные сети".
    print(repr(user_)) #Вывод: SocialMedia(time=100, friends=20, nickname='person')

    user = VK(360, 100, "nika")
    mess = user.send_message("mom") #здесь пишется сообщение
    print(str(user)) #Вывод: Дочерний класс "ВКонтакте".
    print(repr(user)) #Вывод: VK(time=360, friends=100, nickname='nika')

