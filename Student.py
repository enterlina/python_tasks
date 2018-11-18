# Помогите Пете написать класс Student.
# Объекты класса должны принимать при создании имя и фамилию студента.
# Объекты класса можно сортировать с помощью стандартной функции sorted(). Сортировка идет сначала по фамилии, потом по имени.
# Строковое представление объекта должно выглядеть так: Name: имя, Surname: фамилия


from operator import attrgetter


class Student:
    def __init__(self, Name, Surname):
        self.Name = Name
        self.Surname = Surname

    def __repr__(self):
        return repr((self.Name, self.Surname))


student_objects = [
    Student('Steven', 'King'),
    Student('Alex', 'King'),
    Student('Scarlet', 'Johanson'),
    Student('Elisabet', 'Konopily'),
]

student_objects = sorted(student_objects, key=attrgetter('Surname', 'Name'))
print(student_objects)

