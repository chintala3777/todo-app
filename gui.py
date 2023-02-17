import functions
import PySimpleGUI as sg
import time

sg.theme('NeutralBlue')

date_time_label = sg.Text('', key="date_time")
label = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add", size=10)

list_box = sg.Listbox(values=functions.get_read_file(),
                      key="list_items",
                      enable_events=True,
                      size=[50, 20]
                      )
edit_btn = sg.Button("Edit", size=10)
complete_btn = sg.Button("Complete", size=10)
exit_btn = sg.Button("Exit", size=10)
# window = sg.Window('My To-Do App', layout=[[label, input_box]])
window = sg.Window('My To-Do App',
                   layout=[
                       [date_time_label],
                       [label],
                       [input_box, add_button],
                       [list_box, edit_btn, complete_btn],
                       [exit_btn]
                   ],
                   font=["Helvetica", 15]
                   )

while True:
    event, values = window.read(timeout=200)
    window['date_time'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(1, event)
    # print(2, values)
    # print(3, values['list_items'][0])

    match event:
        case "Add":
            todos = functions.get_read_file()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.get_write_file(todos)
            window['list_items'].update(values=todos)
        case "Edit":
            try:
                todo_edit = values["list_items"][0]
                new_todos = values['todo']
                todos = functions.get_read_file()
                index = todos.index(todo_edit)
                todos[index] = new_todos + "\n"
                functions.get_write_file(todos)
                window['list_items'].update(values=todos)
            except IndexError:
                sg.popup("Please select item first", font=["Helvetica", 15])
        case "Complete":
            try:
                todo_complete = values["list_items"][0]
                todos = functions.get_read_file()
                todos.remove(todo_complete)
                functions.get_write_file(todos)
                window['list_items'].update(values=todos)
                window['todo'].update('')
            except IndexError:
                sg.popup("Please select item first", font=["Helvetica", 15])
        case "Exit":
            break
        case 'list_items':
            window['todo'].update(value=values['list_items'][0])
        case sg.WIN_CLOSED:
            break
window.close()
