import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout = [[sg.Text("あなたの出生の秘密をお答えしましょう")],
          [sg.Text("あなたは何歳"),sg.Input("30",key="in1")],
          [sg.Text("お母さんは何歳"),sg.Input("60",key="in2")],
          [sg.Button("実行",key="btn")],
          [sg.Text(key="txt")]]

window = sg.Window("出生の秘密アプリ",layout,
                   font=(None,14),size=(420,170))

def execute():
    in1 = int(values["in1"])
    in2 = int(values["in2"])
    txt = f"お母さんが{in2 - in1}のとき、あなたを産みましたよ。"
    window["txt"].update(txt)

while True:
    event, values = window.read()
    if event == "btn":
        execute()
    if event == None:
        break

window.close()