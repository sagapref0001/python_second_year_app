import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout = [[sg.Text("指定された年の干支を調べます。")],
          [sg.Text("西暦何年ですか？"),sg.Input("2023",key="in1")],
          [sg.Button("実行",key="btn")],
          [sg.Text(key="txt")]]
window = sg.Window("干支調べアプリ",layout,
                font=(None,14), size=(470,170))

def execute():
    eto = ["申","酉","戌","亥","子","丑","寅","卯","辰","巳","午","羊"]
    in1 = int(values["in1"])
    txt = f"{in1}年は{eto[in1 % 12]}年です。"
    window["txt"].update(txt)

while True:
    event, values = window.read()
    if event == "btn":
        execute()
    if event == None:
        break
window.close()
