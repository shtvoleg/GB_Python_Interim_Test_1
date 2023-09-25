# Обучающийся: ШИТОВ Олег Владимирович, "Разработчик Python", поток 4544, будни, утро.  13.08.2023.

# Промежуточная контрольная работа по блоку специализация

# Напишите проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список заметок, редактировать заметку, удалять заметку.
# Подробнее:
# Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок.
# Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки.
# Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может делать как ему удобнее, можно делать как
# параметры запуска программы (команда, данные), можно делать как запрос команды с консоли и последующим вводом данных,
# как-то ещё, на усмотрение студента.

import json
from datetime import datetime

#Функция для загрузки заметок из файла 
def load_notes():
    try:
        with open("Notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = {}
    return notes

#Функция для сохранения заметок в файл
def save_notes(notes):
    with open("Notes.json", "w") as file:
        json.dump(notes, file)

#Функция для вывода меню и возвращения выбранного пункта
def show_menu():
    print("Меню:")
    print("1. Вывести список заметок.")
    print("2. Создать заметку.")
    print("3. Редактировать заметку.")
    print("4. Удалить заметку.")
    print("5. Выход.")
    choice = input("Выберите пункт меню: ")
    return choice

#Функция для вывода списка заметок
def show_notes(notes):
    if not notes:
        print("Список заметок пуст.")
    else:
        print("Список заметок:")
    for title in notes:
        print("*", title)

#Функция для создания заметки
def create_note(notes):
    title = input("Введите название заметки: ")
    content = input("Введите содержимое заметки: ")
    timestamp = datetime.now().strftime('%a %d %b %Y, %I:%M%p')
    print(timestamp)
    notes[title] = [content,timestamp]
    print("Заметка успешно создана.")

#Функция для редактирования заметки
def edit_note(notes):
    title = input("Введите название заметки для редактирования: ")
    if title in notes:
        content = input("Введите новое содержимое заметки: ")
        timestamp = datetime.now()
        notes[title] = [content, timestamp]
        print("Заметка успешно отредактирована.")
    else:
        print("Заметка с таким названием не найдена.")

#Функция для удаления заметки
def delete_note(notes):
    title = input("Введите название заметки для удаления: ")
    if title in notes:
        del notes[title]
        print("Заметка успешно удалена.")
    else:
        print("Заметка с таким названием не найдена.")

#Основная функция программы
def main():
    notes = load_notes()
    while True:
        choice = show_menu()
        if choice == "1":
            show_notes(notes)
        elif choice == "2":
            create_note(notes)
        elif choice == "3":
            edit_note(notes)
        elif choice == "4":
            delete_note(notes)
        elif choice == "5":
            save_notes(notes)
            print("Программа завершена.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

main()