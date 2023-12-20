import PySimpleGUI as sg
from pathlib import Path
import chardet
sg.theme("DarkBrown3")

layout = [[sg.Button("ファイルを開く",key="btn1"),sg.Text(key="txt1")],
          [sg.Multiline(key="txt2",font=(None,14),size=(80,15))]]

window = sg.Window("テキストファイルの読み込み",layout)

def load_text():
    global load_name, enc
    load_name = sg.popup_get_file("テキストを選択してください")
    if load_name == None:
        return
    with open(load_name,"rb") as f:
        b = f.read()
        enc = chardet.detect(b)["encoding"]
        p = Path(load_name)
        txt = p.read_text(encoding = enc)
        window["txt1"].update(load_name)
        window["txt2"].update(txt)

while True:
    event, values = window.read()
    if event == "btn1":
        load_text()
    if event == None:
        break
window.close()