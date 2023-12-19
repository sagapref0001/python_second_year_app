import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout = [[sg.T("金額と人数を入力してください。")],
          [sg.T("金額"),sg.Input(key="in1")],
          [sg.T("人数"),sg.Input(key="in2")],
          [sg.B("実行", k="btn"),sg.T(k="txt")]]
window = sg.Window("割り勘アプリ", layout,
                   font=(None, 14), size=(320,300))

def execute():
    in1 = int(values["in1"])
    in2 = int(values["in2"])
    txt = f"1人、{in1 / in2 :.2f}円です。"
    window["txt"].update(txt)

while True:
    event, values = window.read()
    if event == "btn":
        execute()
    if event == None:
        break
window.close()