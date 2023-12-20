import PySimpleGUI as sg

savename = sg.popup_get_file("名前を付けて保存してください",
                             default_path= "text.txt", save_as=True)
print(savename)