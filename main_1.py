import os
import re
from datetime import datetime

# Функция для создания заметки по запросу пользователя
def build_note(note_text, note_name):
    """Создаёт заметку с указанным текстом и именем."""
    # Очищаем имя от спецсимволов (оставляем только буквы, цифры, пробелы и дефисы)
    note_name = re.sub(r'[^\w\s-]', '', note_name).strip()

    if not note_name:
        print("Ошибка: название заметки не может быть пустым.")
        return

    if len(note_name) > 100:
        print("Название слишком длинное (максимум 100 символов).")
        return

    try:
        with open(f"{note_name}.txt", "w", encoding="utf-8") as file:
            file.write(note_text)
        print(f"Заметка '{note_name}' создана.")
    except PermissionError:
        print("Ошибка: нет прав на запись в текущую директорию.")
    except Exception as e:
        print(f"Ошибка при создании заметки: {e}")

# Функция для запроса названия и текста заметки
def create_note():
    """Запрашивает у пользователя название и текст заметки, создаёт заметку."""
    try:
        note_name = input("Введите название заметки: ").strip()
        note_text = input("Введите текст заметки: ")
        build_note(note_text, note_name)
    except KeyboardInterrupt:
        print("\nОперация отменена пользователем.")
    except Exception as e:
        print(f"Ошибка при вводе данных: {e}")

# Функция вывода заметки по запросу пользователя
def read_note():
    """Читает и выводит содержимое указанной заметки."""
    try:
        note_name = input("Введите название заметки для чтения: ").strip()

        if not note_name:
            print("Название заметки не может быть пустым.")
            return

        # Очищаем имя
        note_name = re.sub(r'[^\w\s-]', '', note_name)
        file_name = f"{note_name}.txt"

        if os.path.isfile(file_name):
            with open(file_name, "r", encoding="utf-8") as file:
                content = file.read()
            print(f"\nСодержимое заметки '{note_name}':\n{content}")
        else:
            print(f"Заметка '{note_name}' не найдена.")
    except KeyboardInterrupt:
        print("\nОперация отменена пользователем.")
    except Exception as e:
        print(f"Ошибка при чтении заметки: {e}")

# Функция редактирования заметки по запросу пользователя
def edit_note():
    """Редактирует указанную заметку."""
    try:
        note_name = input("Введите название заметки для редактирования: ").strip()

        if not note_name:
            print("Название заметки не может быть пустым.")
            return

        # Очищаем имя
        note_name = re.sub(r'[^\w\s-]', '', note_name)
        file_name = f"{note_name}.txt"

        if os.path.isfile(file_name):
            with open(file_name, "r", encoding="utf-8") as file:
                content = file.read()
            print(f"Текущее содержимое заметки '{note_name}':\n{content}")

            new_text = input("Введите новый текст заметки: ")
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(new_text)
            print(f"Заметка '{note_name}' успешно обновлена.")
        else:
            print(f"Заметка '{note_name}' не найдена.")
    except KeyboardInterrupt:
        print("\nОперация отменена пользователем.")
    except Exception as e:
        print(f"Ошибка при редактировании заметки: {e}")

# Функция удаления заметки по запросу пользователя
def delete_note():
    """Удаляет указанную заметку после подтверждения."""
    try:
        note_name = input("Введите название заметки для удаления: ").strip()

        if not note_name:
            print("Название заметки не может быть пустым.")
            return

        # Очищаем имя
        note_name = re.sub(r'[^\w\s-]', '', note_name)
        file_name = f"{note_name}.txt"

        if os.path.isfile(file_name):
            confirm = input(f"Удалить заметку '{note_name}'? (да/нет): ").strip().lower()
            if confirm != 'да':
                print("Удаление отменено.")
                return

            os.remove(file_name)
            print(f"Заметка '{note_name}' успешно удалена.")
        else:
            print(f"Заметка '{note_name}' не найдена.")
    except KeyboardInterrupt:
        print("\nОперация отменена пользователем.")
    except Exception as e:
        print(f"Ошибка при удалении заметки: {e}")

# Функция вывода всех заметок пользователя
def display_notes():
    """Выводит список всех заметок, отсортированных по длине названия."""
    try:
        # Получаем все .txt файлы в текущей директории
        note_files = [f for f in os.listdir() if f.endswith('.txt') and os.path.isfile(f)]


        if not note_files:
            print("Заметок не найдено.")
            return

        # Сортируем по длине имени (без расширения)
        sorted_notes = sorted(note_files, key=lambda x: len(os.path.splitext(x)[0]))

        print("\nСписок всех заметок (отсортировано по длине названия):")
        for note in sorted_notes:
            name_without_ext = os.path.splitext(note)[0]
            # Получаем время последнего изменения
            stat = os.stat(note)
            modified = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M")
            print(f"{name_without_ext} (обновлено: {modified})")
    except KeyboardInterrupt:
        print("\nОперация отменена пользователем.")
    except Exception as e:
        print(f"Ошибка при отображении заметок: {e}")

# Главное меню программы
def main():

    print("Менеджер заметок v1.0")
    while True:
        print("\n" + "="*40)
        print("1. Создать заметку")
        print("2. Читать заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Показать все заметки")
        print("6. Выход")
        print("="*40)

        try:
            choice = input("Выберите действие (1-6): ").strip()

            if choice == "1":
                create_note()
            elif choice == "2":
                read_note()
            elif choice == "3":
                edit_note()
            elif choice == "4":
                delete_note()
            elif choice == "5":
                display_notes()
            elif choice == "6":
                print("До свидания!")
                break
            else:
                print("Неверный выбор. Введите число от 1 до 6.")
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем. До свидания!")
            break
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()
