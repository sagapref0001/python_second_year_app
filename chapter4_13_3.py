import PySimpleGUI as sg
import datetime

layout = [[sg.Text(font=("Arial",40),k="txt",
           size=(20,1), justification="center")]]
window = sg.Window("時計テスト",layout,size=(320,80),keep_on_top=True)

c = 0

while True:
    event, values = window.read(timeout=500)
    c = c + 1
    window["txt"].update(f"{c}")
    if event == None:
        break
window.close()