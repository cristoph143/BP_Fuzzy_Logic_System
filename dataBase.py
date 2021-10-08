class Personal_Info:
    info = []

    def __init__(self, my_name, my_age, my_gender):
        self.name = my_name
        self.age = my_age
        self.gender = my_gender
        self.info.append(self.name)
        self.info.append(self.age)
        self.info.append(self.gender)

    @property
    def get_name(self):
        return self.name

    def set_name(self, f_name):
        self.name = f_name

    @property
    def get_age(self):
        return self.age

    def set_age(self, ages):
        self.age = ages

    @property
    def get_gender(self):
        return self.age

    def set_gender(self, genders):
        self.gender = genders

    def hello(self):
        print('Welcome to Python ' + self.name + '!')
        print('In ' + str(self.age) + ' years of existence as a ' + str(self.gender) +
              '!You will discovered how your BP will work! Congrats!!!')


class BP:
    def __init__(self, sys, dia):
        self._name = Personal_Info.get_name
        self._gender = Personal_Info.get_gender
        self._age = Personal_Info.get_age
        self._systolic = sys
        self._diastolic = dia

    def get_systolic(self):
        return self._systolic

    def set_systolic(self, sys):
        self._systolic = sys

    def get_diastolic(self):
        return self._diastolic

    def set_diastolic(self, dia):
        self._diastolic = dia

    def status(self, name):
        print(name + ', you have ' + str(self._systolic) + ' / ' + str(self._diastolic))
