import PySimpleGUI as sg
from PIL import Image
import io
sg.theme("DarkBrown3")

layout = [[sg.Button("ファイルを開く",key="btn1"),sg.T(key="txt")],
          [sg.Image(key="img")]]
window = sg.Window("画像ファイルを表示",layout,size=(300,400))

def load_image():
    load_name = sg.popup_get_file("画像ファイルを選択してください")
    if not load_name:
        return
    try:
        img = Image.open(load_name)
        img.thumbnail((300,300))
        bio = io.BytesIO()
        img.save(bio,format="PNG")
        window["img"].update(data=bio.getvalue())
        window["txt"].update(load_name)
    except:
        window["img"].update()
        window["txt"].update("失敗しました。")

while True:
    event, values = window.read()
    if event == "btn1":
        load_image()
    if event == None:
        break

window.close()

