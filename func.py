FILEPATH = "todo.txt"


def get_todos(filepath=FILEPATH):
    """Reads the text file and returns them as a list."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """Writes the todos list in a text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_local)
