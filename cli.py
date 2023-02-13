from functions import get_read_file, get_write_file
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
# print("it is", now)
print(f"it is {now} ")

while True:
    user_action = input("Type add or show or edit or complete or exit : ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        todos = get_read_file()
        todos.append(todo)

        get_write_file(todos)

    elif user_action.startswith('show'):
        todos = get_read_file()
        # comprehension list
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_read_file()

            new_todo = input("Enter new todo : ")
            todos[number] = new_todo + '\n'

            get_write_file(todos)

        except ValueError:
            print("invalid command")
            continue


    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_read_file()
            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            get_write_file(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except (IndexError, ValueError):
            print("There is no item with that number")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")

print('Bye!')
