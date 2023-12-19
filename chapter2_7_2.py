import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout = [[sg.Text("テキスト")],
          [sg.Input("入力欄")],
          [sg.Multiline("複数行テキスト １行目\n２行目", size=(30,3))],
          [sg.Image("futaba.png")]]
window = sg.Window("入力欄テスト",layout,
                   font=(None,14), size=(300,240))

event, values = window.read()
window.close()