import os
from Rational_list import RationalList


def run_task(filename):
    if not os.path.exists(filename):
        print(f"Файл {filename} не знайдено.")
        return

    r_list = RationalList()

    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            for p in parts:
                if p:
                    r_list += p

    total = r_list.get_sum()
    print(f"Дані з файлу: {filename}")
    print(f"Кількість чисел: {len(r_list)}")
    print(f"Сума (дріб): {total}")
    print(f"Сума (десяткова): {total():.4f}")

if __name__ == "__main__":
    files = ["input01.txt", "input02.txt", "input03.txt"]
    for f in files:
        run_task(f)
