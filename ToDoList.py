tasks_list = []

description = """
Выберите действие:
1. Добавить задачу
2. Просмотреть список задач
3. Удалить задачу
4. Выйти из программы

Ваш выбор: """

def view_tasks():
    tasks = ""
    for id, task in enumerate(tasks_list):
        tasks += f'\n{id+1}. {task}'
    return tasks

def add_task():
    task_text = input('Введите текст задачи: ')
    tasks_list.append(task_text)
    print('Задача добавлена!')

def delete_task():
    del_request = int(input(f'Список задач: {view_tasks()}\nВыберите номер задачи для удаления: '))
    while True:
        try:
            del tasks_list[del_request-1]
            print('Задача удалена.')
            break
        except:
            print('Такой задачи нет в списке.')

def main():
    while True:
        request = int(input(description))
        try:
            if request == 1:
                add_task()
            if request == 2:
                print(view_tasks())
            if request == 3:
                delete_task()
            if request == 4:
                break
        except:
            print('Такой операции нет.')
    print('Программа завершена.')
    
main()