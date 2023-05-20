# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {"first_name": "Вася"},
    {"first_name": "Петя"},
    {"first_name": "Маша"},
    {"first_name": "Маша"},
    {"first_name": "Петя"},
]
from collections import Counter

names_counter = Counter([student["first_name"] for student in students])
for name, count in names_counter.items():
    print(f"{name}: {count}")


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {"first_name": "Вася"},
    {"first_name": "Петя"},
    {"first_name": "Маша"},
    {"first_name": "Маша"},
    {"first_name": "Оля"},
]
names_counter = Counter([student["first_name"] for student in students])
frequent_name = names_counter.most_common(1)[0][0]
print(f"Самое частое имя среди учеников: {frequent_name}")


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {"first_name": "Вася"},
        {"first_name": "Вася"},
    ],
    [  # это – второй класс
        {"first_name": "Маша"},
        {"first_name": "Маша"},
        {"first_name": "Оля"},
    ],
    [  # это – третий класс
        {"first_name": "Женя"},
        {"first_name": "Петя"},
        {"first_name": "Женя"},
        {"first_name": "Саша"},
    ],
]
for i, group in enumerate(school_students):
    names_counter = Counter([student["first_name"] for student in group])
    frequent_name = names_counter.most_common(1)[0][0]
    print(f"Самое частое имя в классе {i + 1}: {frequent_name}")


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {"class": "2a", "students": [{"first_name": "Маша"}, {"first_name": "Оля"}]},
    {"class": "2б", "students": [{"first_name": "Олег"}, {"first_name": "Миша"}]},
    {
        "class": "2б",
        "students": [
            {"first_name": "Даша"},
            {"first_name": "Олег"},
            {"first_name": "Маша"},
        ],
    },
]
is_male = {
    "Олег": True,
    "Маша": False,
    "Оля": False,
    "Миша": True,
    "Даша": False,
}
for group in school:
    sex_of_students = [is_male[student["first_name"]] for student in group["students"]]

    sex_stat = Counter(sex_of_students)

    class_id = group["class"]
    girls_num = sex_stat[False]
    boys_num = sex_stat[True]

    print(f"Класс {class_id}: девочки {girls_num}, мальчики {boys_num}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {"class": "2a", "students": [{"first_name": "Маша"}, {"first_name": "Оля"}]},
    {"class": "3c", "students": [{"first_name": "Олег"}, {"first_name": "Миша"}]},
]
is_male = {
    "Маша": False,
    "Оля": False,
    "Олег": True,
    "Миша": True,
}
top_boys_num = 0
top_boys_id = ""
top_girls_num = 0
top_girls_id = ""

for group in school:
    sex_of_students = [is_male[student["first_name"]] for student in group["students"]]

    sex_stat = Counter(sex_of_students)
    girls_num = sex_stat[False]
    boys_num = sex_stat[True]

    if girls_num > top_girls_num:
        top_girls_num = girls_num
        top_girls_id = group["class"]

    if boys_num > top_boys_num:
        top_boys_num = boys_num
        top_boys_id = group["class"]

print(f"Больше всего мальчиков в классе {top_boys_id}")
print(f"Больше всего девочек в классе {top_girls_id}")
