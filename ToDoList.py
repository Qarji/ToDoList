import sqlite3
from datetime import datetime

description = """
Выберите действие:
1. Добавить задачу
2. Просмотреть список задач
3. Удалить задачу
4. Выйти из программы

Ваш выбор: """

def view_tasks(cursor):
    tasks = cursor.execute('SELECT rowid, name, body, date FROM Item').fetchall()
    if not tasks:
        return "Список задач пуст."
    return '\n'.join([f'{rowid}. {name} | {body} | {date}' for rowid, name, body, date in tasks])

def add_task(cursor, conn):
    task_name = input('Введите название задачи: ')
    task_text = input('Введите текст задачи: ')
    cursor.execute('INSERT INTO Item (name, body, date) VALUES (?, ?, ?)', (task_name, task_text, datetime.now().strftime('%d.%m.%Y')))
    conn.commit()
    print('Задача добавлена!')

def delete_task(cursor, conn):
    while True:
        try:
            del_request = int(input(f'Список задач: {view_tasks()}\nВыберите номер задачи для удаления: '))
            cursor.execute('SELECT 1 FROM Item WHERE rowid = ?', (del_request,))
            if cursor.fetchone() is None:
                print('Такой задачи нет в списке.')
            else:
                cursor.execute('DELETE FROM Item WHERE rowid = ?', (del_request,))
                conn.commit()
                print('Задача удалена успешно.')
                break
        except ValueError:
            print('Введите корректное число.')

def main():
    with sqlite3.connect('Tasks.db') as conn:
        cursor = conn.cursor()
        actions = {
            1: lambda: add_task(cursor, conn),
            2: lambda: print(view_tasks(cursor)),
            3: lambda: delete_task(cursor, conn),
        }
        
        while True:
            try:
                request = int(input(description))
                if request == 4:
                    break
                action = actions.get(request)
                if action:
                    action()
            except:
                print('Такой команды нет.')
        print('Программа завершена.')
main()