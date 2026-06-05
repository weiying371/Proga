from student import Student
from visitors import Professor, Accounting, Parents, Canteen, Dormitory


def run_simulation(file_lines):
    direction = file_lines[0].strip()
    required_credits = int(file_lines[1].strip())
    initial_money = int(file_lines[2].strip())

    student = Student(direction, required_credits, initial_money)

    for line in file_lines[3:]:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        action = parts[0]

        if action == "Professor":
            student.accept(Professor(parts[1], int(parts[2])))
        elif action == "Accounting":
            student.accept(Accounting(int(parts[1])))
        elif action == "Parents":
            student.accept(Parents(int(parts[1])))
        elif action == "Canteen":
            student.accept(Canteen(int(parts[1])))
        elif action == "Dormitory":
            student.accept(Dormitory(int(parts[1])))

    if student.is_expelled:
        print("Статус: Відраховано (Брак коштів на їжу чи проживання).")
        print("Диплом: Не отримано.")
    elif student.has_graduated():
        print("Статус: Успішно випущений!")
        print(f"Диплом: Отримано (Кредити: {student.credits}/{student.required_credits}).")
    else:
        print("Статус: Навчання завершилось.")
        print(f"Диплом: Не отримано (Недостатньо кредитів: {student.credits}/{student.required_credits}).")

    print(f"Фінальний баланс грошей: {student.money}")


# Демонстраційний запуск (імітація зчитування файлу типу input01.txt)
if __name__ == "__main__":
    mock_input_file = [
        "mixed",  # Напрям студента
        "60",  # Потрібно кредитів
        "500",  # Стартовий капітал
        "Parents 1000",  # +1000 від батьків (Разом 1500)
        "Professor humanitarian 40",  # +40 кредитів (Разом 40)
        "Canteen 200",  # -200 за їжу (Разом 1300)
        "Professor natural 30",  # +30 кредитів (Разом 70, умова виконана)
        "Dormitory 400"  # -400 за гуртожиток (Разом 900)
    ]

    run_simulation(mock_input_file)
