import PySimpleGUI as sg
from pathlib import Path
import chardet
sg.theme("DarkBrown3")

layout = [[sg.Button("ファイルを開く",key="btn1"),sg.Text(key="txt1")],
          [sg.Button("ファイルを保存",key="btn2")],
          [sg.Multiline(key="txt2",font=(None,14),size=(80,20))]]
window = sg.Window("テキストファイルの保存",layout,resizable=True)

load_name = None
enc = "UTF-8"
def load_file():
    global load_name, enc
    load_name = sg.popup_get_file("テキストファイルを選択してください")
    if not load_name :
        return
    with open(load_name,"rb") as f:
        b = f.read()
        enc = chardet.detect(b)["encoding"]
        p = Path(load_name)
        txt = p.read_text(encoding=enc)
        window["txt1"].update(load_name)
        window["txt2"].update(txt)

def save_text():
    global load_name, enc
    save_name = sg.popup_get_file("名前を付けてください。",default_path= load_name, save_as=True)
    if not save_name:
        sg.PopupTimed("ファイル名を入力してください")
        return
    if save_name.find(".") == -1:
        save_name = save_name + ".txt"
    p = Path(save_name)
    p.write_text(values["txt2"],encoding=enc)
    window["txt1"].update(save_name)
    load_name = save_name

while True:
    event, values = window.read()
    if event == "btn1":
        load_file()
    if event == "btn2":
        save_text()
    if event == None:
        break
window.close()
