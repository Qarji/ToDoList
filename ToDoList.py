tasks_list = []

description = """
Выберите действие:
1. Добавить задачу
2. Просмотреть список задач
3. Удалить задачу
4. Выйти из программы

Ваш выбор: """
request = int(input(description))

def show_list():
    tasks = ""
    for id, task in enumerate(tasks_list):
        tasks += f'\n{id+1}. {task}'
    return tasks

while request != 4:
    if request == 1:
        task_text = input('Введите текст задачи: ')
        tasks_list.append(task_text)
        print('Задача добавлена!')
    elif request == 2:
        print(f'Список задач:{show_list()}')
    elif request == 3:
        del_request = int(input(f'Список задач: {show_list()}\nВыберите номер задачи для удаления: '))
        try:
            del tasks_list[del_request-1]
            print('Задача удалена.')
        except:
            print('Такой задачи нет в списке.')
    else:
        print('Такой операции нет.')
    request = int(input(description))
    
print('Программа завершена.')