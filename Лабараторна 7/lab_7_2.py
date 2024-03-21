def add(student, key, grade):
    student[key] = grade


def Del(student, key):
    del student[key]
    print("Видалено", key, ".")


def print_sort(student):
    sorted_student = sorted(student.items(), key=lambda x: sum(x[1]), reverse=True)
    sorted_student_dict = dict(sorted_student)

    print("\nВідсортований словник: ")

    for key, value in sorted_student_dict.items():
        print("Оцінки студента ", key, " - ", value)
        total_points = sum(value)
        print("Загальна кількість балів: ", total_points)

    search_key = input("Введіть фамілію студента для пошуку в ТОПІ, також студеньів які набрали менше балів: ")
    if search_key in sorted_student_dict:
        place = 1
        for k, v in sorted_student:
            if sum(sorted_student_dict[search_key]) < sum(v):
                place += 1
        print("Місце студента", search_key, ":", place)

        lower_student = [k for k, v in sorted_student if sum(v) < sum(sorted_student_dict[search_key])]
        if lower_student:
            print("Студенти, що набрали менше балів:")
            for team in lower_student:
                print(team)
        else:
            print("Немає студентів, що набрали менше балів.")
    else:
        print("Студента не знайдено не знайдена.")


student = {}

num_of_student = int(input("Введіть кількість студентів: "))
for _ in range(num_of_student):
    student_name = input("Введіть фамілію студента: ")
    num_of_grades = int(input("Введіть кількість оцінок для студента {}: ".format(student_name)))
    grades = []
    for _ in range(num_of_grades):
        grade = int(input("Введіть оцінку: "))
        grades.append(grade)
    add(student, student_name, grades)
print_sort(student)
