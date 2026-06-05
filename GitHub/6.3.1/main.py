import os
from Rational_list import Rational_list
from Rational import Rational


def run_test(filename):
    if not os.path.exists(filename):
        print(f"Помилка: Файл {filename} не знайдено.")
        return

    r_list = Rational_list()

    with open(filename, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            for part in line.split():
                try:
                    r_list += part
                except ValueError as ve:
                    print(f"Помилка даних у {filename} (рядок {line_num}): {part} - {ve}")
                except Exception as e:
                    print(f"Непередбачена помилка у {filename} (рядок {line_num}): {e}")

    print(f"Результат для {filename}")
    if len(r_list) == 0:
        print("Список порожній (немає коректних даних).")
    else:
        print("Елементи у порядку спадання (знаменник, потім чисельник):")
        for num in r_list:
            print(f"{str(num):7}  чисельник: {num['n']:3}, знаменник: {num['d']:3}")

        try:
            print(f"\nЗагальна сума: {r_list.get_sum()}")
        except Exception as e:
            print(f"Помилка при обчисленні суми: {e}")


if __name__ == "__main__":
    files = ["input01.txt", "input02.txt", "input03.txt"]
    for f in files:
        run_test(f)
