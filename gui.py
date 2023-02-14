import functions
import PySimpleGUI as sg

label = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_read_file(),
                      key="list_items",
                      enable_events=True,
                      size=[50, 20]
                      )
edit_btn = sg.Button("Edit")
# window = sg.Window('My To-Do App', layout=[[label, input_box]])
window = sg.Window('My To-Do App',
                   layout=[
                       [label],
                       [input_box, add_button],
                       [list_box, edit_btn]
                   ],
                   font=["Helvetica", 20]
                   )

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['list_items'][0])

    match event:
        case "Add":
            todos = functions.get_read_file()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.get_write_file(todos)
            window['list_items'].update(values=todos)
        case "Edit":
            todo_edit = values["list_items"][0]
            new_todos = values['todo']

            todos = functions.get_read_file()
            index = todos.index(todo_edit)
            todos[index] = new_todos + "\n"
            functions.get_write_file(todos)
            window['list_items'].update(values=todos)
        case 'list_items':
            window['todo'].update(value=values['list_items'][0])
        case sg.WIN_CLOSED:
            break
window.close()
