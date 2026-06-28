import json
import os

DATA_FILE = "data.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def next_id(data):
    if not data:
        return 1
    return max(item["id"] for item in data) + 1


def add_result():
    data = load_data()

    sport = input("Вид спорту: ").strip()
    if not sport:
        print("Помилка: введіть вид спорту.")
        return

    date = input("Дата (РРРР-ММ-ДД): ").strip()
    if not date:
        print("Помилка: введіть дату.")
        return

    try:
        result = float(input("Результат: "))
    except ValueError:
        print("Помилка: введіть число.")
        return

    unit = input("Одиниця вимірювання: ").strip()
    if not unit:
        print("Помилка: введіть одиницю.")
        return

    record = {
        "id": next_id(data),
        "sport": sport,
        "date": date,
        "result": result,
        "unit": unit
    }

    data.append(record)
    save_data(data)
    print("✓ Результат додано.")


def show_results():
    data = load_data()

    if not data:
        print("Записів немає.")
        return

    print("\nID | Вид спорту | Дата | Результат")
    print("-" * 45)

    for item in data:
        print(
            f"{item['id']} | "
            f"{item['sport']} | "
            f"{item['date']} | "
            f"{item['result']} {item['unit']}"
        )


def show_dynamics():
    sport = input("Введіть вид спорту: ").strip()

    data = load_data()
    results = [x for x in data if x["sport"].lower() == sport.lower()]

    if not results:
        print("Результатів не знайдено.")
        return

    results.sort(key=lambda x: x["date"])

    print("\nДинаміка результатів:")
    for item in results:
        print(
            f"{item['date']} - "
            f"{item['result']} "
            f"{item['unit']}"
        )


def best_result():
    sport = input("Введіть вид спорту: ").strip()

    data = load_data()
    results = [x for x in data if x["sport"].lower() == sport.lower()]

    if not results:
        print("Результатів не знайдено.")
        return

    best = max(results, key=lambda x: x["result"])

    print("\nНайкращий результат:")
    print(
        f"{best['sport']} - "
        f"{best['result']} "
        f"{best['unit']} "
        f"({best['date']})"
    )


def delete_result():
    try:
        record_id = int(input("ID запису: "))
    except ValueError:
        print("Помилка: введіть число.")
        return

    data = load_data()
    new_data = [x for x in data if x["id"] != record_id]

    if len(new_data) == len(data):
        print("Запис не знайдено.")
        return

    save_data(new_data)
    print("✓ Запис видалено.")


def menu():
    while True:
        print("\n===== ТРЕКЕР СПОРТРЕЗУЛЬТАТІВ =====")
        print("1. Додати результат")
        print("2. Переглянути всі результати")
        print("3. Переглянути динаміку")
        print("4. Найкращий результат")
        print("5. Видалити запис")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            add_result()
        elif choice == "2":
            show_results()
        elif choice == "3":
            show_dynamics()
        elif choice == "4":
            best_result()
        elif choice == "5":
            delete_result()
        elif choice == "0":
            break
        else:
            print("Невірний вибір.")


if __name__ == "__main__":
    menu()
