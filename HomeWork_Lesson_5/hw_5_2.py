class hw_error(Exception):
    """Класс ошибок, нужен для выведения наших ошибок"""
    pass


class Person:
    def __init__(self, full_name, born_date):
        self.full_name = self.check_full_name(full_name)
        self.born_date = self.check_born_date(born_date)

    def check_full_name(self, full_name):
        """Метод проверяет правильность заполнения поля Имя и фамилия. В случае неправильного ввода возвращает ошибку"""
        if len(full_name.split()) == 2:
            return full_name
        else:
            raise hw_error(f'\n{"=" * 50}\n|| Вы должны передавать два слова: Имя и фамилию.||\n{"=" * 50}')

    def check_born_date(self, born_date):
        """Метод проверяет правильность заполнения поля Дня рождения. В случае если год больше 2021 или меньше 1900 возвращает ошибку"""
        if born_date > 2021:
            raise hw_error(f'\n{"=" * 50}\n||        Сожелеем но Вы еще не рождены.        ||\n{"=" * 50}')
        elif born_date < 1900:
            raise hw_error(
                f'\n{"=" * 65}\n||  Проверьте дату своего рождения она должна быть позже 1900  ||\n{"=" * 65}')
        else:
            return born_date

    def only_name(self):
        return self.full_name.split()[0]

    def surname(self):
        return self.full_name.split()[0]

    def how_old(self, date=2021):
        return date - self.born_date


class Employee(Person):
    def __init__(self, full_name, born_date, position, work_experience, salary):
        super().__init__(full_name, born_date)
        self.position = position
        self.work_experience = self.check_work_experience(work_experience)
        self.salary = self.check_salary(salary)

    def check_work_experience(self, work_experience):
        """Метод проверяет  правильность заполнения поля рабочий опыт. В случае отрицательного значения возвращает ошибку"""
        if work_experience < 0:
            raise hw_error(f'\n{"=" * 60}\n|| Опыт может быть нулевым, но не может быть отрицательным ||\n{"=" * 60}')
        else:
            return work_experience

    def check_salary(self, salary):
        """Метод проверяет правильность заполнения поля ЗП. В случае отрицательного значения возвращает ошибку"""
        if salary < 0:
            raise hw_error(
                f'\n{"=" * 75}\n||   Мы Вам платим, а не Вы нам! Введите зарплату равну или больше нуля. ||\n{"=" * 75}')
        else:
            return salary

    def position_and_level(self):
        """Метод выводить уровень и позицию сотрудника опираясь на введеные данные и опыт работы"""
        if self.work_experience < 3:
            level = 'Junior'
        elif 6 > self.work_experience >= 3:
            level = 'Middle'
        elif self.work_experience >= 6:
            level = 'Senior'
        return f'{level} {self.position}'

    def salary_up(self, bonus):
        """Метод увеличивает значение ЗП на введеное пользователем значение."""
        self.salary += bonus


class ITEmployee(Employee):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skills = []

    def new_skill(self, skill):
        """Метод добавляет один Скил"""
        self.skills.append(skill)

    def new_skills(self, *args):
        """Метод добавляет несколько скилов"""
        self.skills.extend(args)


p = Person('Bori Jonson', 2005)
print(p.only_name())
print(p.how_old())
print(p.how_old(2031))
t = Employee('Bori Jonson', 2005, 'developer', 6, 2323)
print(t.position_and_level())
print(t.salary)
t.salary_up(1000)
print(t.salary)
d = ITEmployee('Bori Jonson', 2005, 'developer', 6, 2323)
print(d.skills)
d.new_skill('Умеет красить')
print(d.skills)
d.new_skills('Умеет красть', 'Умеет есть ногами')
print(d.skills)
