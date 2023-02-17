FILEPATH = "todos.txt"


def get_read_file(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def get_write_file(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("hello")