import PySimpleGUI as sg
import datetime

layout = [[sg.Text("0:00:00:000000",font=("Arial",40),key="txt",
                  size=(20,1),justification="center")],
          [sg.Push(),sg.Button("START/STOP",key="btn"),sg.Push()]]
window = sg.Window("ストップウォッチ",layout,font=(None,14),size=(400,130),keep_on_top=True)


def execute():
    if start_flag == True:
        now = datetime.datetime.now()
        stop_time = now - start_time
        window["txt"].update(stop_time)
def startstop():
    global start_time, start_flag
    if start_flag == True:
        start_flag = False
    else:
        start_time = datetime.datetime.now()
        start_flag = True

start_flag = False
start_time = None

while True:
    event, values = window.read(timeout=50)
    execute()
    if event == "btn":
        startstop()
    if event == None:
        break

window.close()