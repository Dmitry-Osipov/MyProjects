from string import ascii_letters


class Person:
    """
    Требуется создать класс Person, который будет содержать следующие данные:
    ФИО, возраст (целое число от 14 до 120), серию и номер паспорта в формате xxxx xxxxxx (x - целое число от 0 до 9),
    вес в кг (вещественное число от 20)
    """
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчщшъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, passport, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_passport(passport)
        self.verify_weight(weight)
        # Если при вызове методов выше не возникнет ни одного исключения, то программа пойдёт
        # дальше. Если же возникнет, то мы увидим его в консоли, и программа завершит свою работу.

        """
        Если ниже все данные будут не приватными, а публичными, то программа получит большую функциональность, 
        т.е. мы не будем записывать напрямую в какую-то частное локальное свойство какое-то значение, а сразу пропишем
        объект свойства (уберём 2 подчёркивания) и присвоим новое значение. Тогда будет вызван соответствующий сеттер, 
        а проверку выше мы сможем убрать (ибо эта проверка есть в сеттере). Всё сказанное до этого не относится к ФИО,
        ведь для него не прописан сеттер. Упрощённый код будет выглядеть так:
        
        ...
        self.verify_fio(fio)
        
        self.__fio = fio.split()
        self.old = old
        self.passport = passport
        self.weight = weight
        ...
        """
        self.__fio = fio.split()
        self.__old = old
        self.__passport = passport
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')

        fio_list = fio.split()
        if len(fio_list) != 3:
            raise TypeError('Неверный формат записи ФИО')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for item in fio_list:
            if len(item) < 1:
                raise TypeError('В ФИО должен быть хотя бы один символ')
            if len(item.strip(letters)) != 0:  # если в ФИО содержит только разрешённые символы, то strip их все удалит,
                # и длина полученной строки должна быть равна нулю
                raise TypeError('В ФИО можно использовать только буквенные символы и дефис')

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or 120 < old < 14:
            raise TypeError('Возраст должен быть целым числом в диапазоне от 14 до 120')

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError('Вес должен быть вещественным числом от 20')

    @classmethod
    def verify_passport(cls, passport):
        if type(passport) != str:
            raise TypeError('Паспорт должен быть строкой')

        passports_serial_and_number = passport.split()
        if (len(passports_serial_and_number) != 2 or len(passports_serial_and_number[0]) != 4
                or len(passports_serial_and_number[1]) != 6):
            raise TypeError('Неверный формат паспорта')

        for digit in passports_serial_and_number:
            if not digit.isdigit():
                raise TypeError('Серия и номер паспорта должны быть числами')

    @property
    def fio(self):  # В рамках учебного примера не будем прописывать сеттер. Будем считать, что ФИО не меняется
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.verify_passport(passport)
        self.__passport = passport

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight


me = Person('Осипов Дмитрий Романович', 22, '1234 567890', 80.2)
me.old = 100
me.passport = '1212 898190'
me.weight = float(78)
print(me.__dict__)
