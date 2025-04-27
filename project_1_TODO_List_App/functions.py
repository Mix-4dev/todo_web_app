FILEPATH = 'db.txt' # Constant variables
if __name__ == 'functions':
    def read_todos(file_path = FILEPATH):
        """Read a text file and
        return a list of todos"""
        with open(file = file_path, mode = 'r') as file:
            todos_local: list[str] = file.readlines()
        return todos_local

    def write_todos(todos_arg, file_path = FILEPATH):
        """Write todos to a text file"""
        with open(file = file_path, mode = 'w') as file:
            file.writelines(todos_arg)

if __name__ == '__main__':
    print("hello from script")
