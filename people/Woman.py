from PythonLearn.people.Human import Human
from random import randint


class Woman(Human):

    def __init__(self, name='Masha'):
        super().__init__(name)
        self.hairColor = 'blond'

    def shopping(self, man):
        if isinstance(man, Human):
            if man.money > 0:
                print(self.name + 'say: need ur money!!!')
            else:
                print(self.name + 'say: earn the fcking money!!!')

    @staticmethod
    def sex(father, mother, name='Не выбрали'):
        if isinstance(father, Human) and isinstance(mother, Woman):
            genders = ['Мужчина', 'Женщина']
            gender = genders[randint(0, 1)]
            if gender == 'Мужчина':
                names = ['Валерий', 'Кирилл', 'Стас', 'Виктор', 'Матвей',
                         'Евгений', 'Дмитрий', 'Александр', 'Анатолий', 'Генадий']
            else:
                names = ['Светлана', 'Виктория', 'Алиса', 'Марина', 'Анна', 'Злата',
                         'Дарья', 'Елизавета', 'Ирина', 'Мария', 'Александра', 'Евгения']
            name = names[randint(0, len(names) - 1)]
            print('Имя ребёнка: ' + name)
            print('Пол ребёнка: ' + gender)
            return Human(name)
        else:
            print('ну ты и извращуга!!!')