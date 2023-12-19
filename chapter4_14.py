import PySimpleGUI as sg
import datetime

layout = [[sg.Text("0000/00/00 (---)",font=("Arial",30), key="txt2",
                size=(20,1),justification="center")],
          [sg.Text("AM:00:00:00",font=("Arial",40),key="txt1",
                size=(20,1), justification="center")]]
window = sg.Window("時計",layout,size=(400,160),keep_on_top=True)

def execute():
    now = datetime.datetime.now()
    window["txt2"].update(f"{now:%Y/%m/%d (%a)}")
    window["txt1"].update(f"{now:%H:%M:%S}")


while True:
    event, values = window.read(timeout=1000)
    execute()
    if event == None:
        break

window.close()