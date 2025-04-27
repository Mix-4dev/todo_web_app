import functions # local module
import time # global module
now = time.strftime("%B %d, %Y %H:%M:%S")
print(f"It is {now}")
prompt_input_action:str = "Type add, show, edit, complete, exit: "
while True:
    user_action: str = input(prompt_input_action).strip().lower()  # TODO: "Type add, show, edit, complete, exit: "

    if user_action.startswith('add'):
            todos_list: list[str] = functions.read_todos() # () as it's a function call
            todos_list.append(user_action[4:]+ '\n')
            functions.write_todos(todos_list)

    elif user_action.startswith('show'):
            todos_list: list[str] = functions.read_todos()
            if len(todos_list) == 0:
                print(f"your to todos is empty -> {todos_list}")

            new_todos_list: list= [item.rstrip('\n') for item in todos_list]
            for index, item in enumerate(iterable= new_todos_list, start = 1):
                print(f"{index}- {item}")

    elif user_action.startswith('edit'):

            todos_list: list[str] = functions.read_todos()

            new_todo:str = input("Enter a New todo: ")
            try: # edit 2
                todos_list[ int(user_action[5:]) -1 ]= new_todo  + '\n'
                print("The todo is edited successfully")
            except ValueError:
                print("Your command is invalid")
                continue

            print(f"the edited version of todos ==> {todos_list}")

            functions.write_todos(todos_list)

    elif user_action.startswith('complete'):
            todos_list: list[str] = functions.read_todos()
            try: # complete 5
                return_pop = todos_list.pop(int(user_action [9:]) - 1).strip('\n')
                print(f"You complete {return_pop} task successfully :)")

            except IndexError:
                print(f'you just have {len(todos_list)} tasks.')

            functions.write_todos(todos_list)

    elif user_action.startswith('exit'):break
    else:print("Command is not valid")
print('Exit say Bye')
print("Im out of loop scope")