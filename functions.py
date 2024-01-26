def get_todos(file='todos.txt'):
    with open(file, 'r') as file:
       list = file.readlines()
    return list

def write_todos(list, file='todos.txt'):
    with open(file, 'w') as file:
        file.writelines(list)

