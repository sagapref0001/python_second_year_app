import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout = [[sg.Text("身長と体重を入力してください。")],
          [sg.Text("身長cm"),sg.Input("160",key="in1")],
          [sg.Text("体重kg"),sg.Input("60",key="in2")],
          [sg.Button("実行",key="btn"),sg.T(key="txt")]]
window = sg.Window("BMI計算アプリ",layout,
                   font=(None,14), size=(320,150))

def execute():
    in1 = float(values["in1"])/100.0
    in2 = float(values["in2"])
    bmi = in2 / (in1 * in1)
    txt = f"BMI値は、{bmi:.2f}です。"
    window["txt"].update(txt)

while True:
    event, values = window.read()
    if event == "btn":
        execute()
    if event == None:
        break
window.close()
