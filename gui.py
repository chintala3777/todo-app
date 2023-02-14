import functions
import PySimpleGUI as sg

label = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")

# window = sg.Window('My To-Do App', layout=[[label, input_box]])
window = sg.Window('My To-Do App',
                   layout=[
                       [label],
                       [input_box, add_button]
                   ],
                   font=["Helvetica", 20]
                   )

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_read_file()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.get_write_file(todos)
        case sg.WIN_CLOSED:
            break
window.close()
