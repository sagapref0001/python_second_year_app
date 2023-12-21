import PySimpleGUI as sg
from PIL import Image
import io

sg.theme("DarkBrown3")
layout = [[sg.Button("ファイルを開く",key="btn1"),sg.Text(key="txt")],
          [sg.Button("ファイルを保存",key="btn2")],
          [sg.Image(key="img")]]
window = sg.Window("モノクロ画像に変換",layout, size=(400,500))

def load_image():
    global img
    load_name = sg.popup_get_file("画像ファイルを選択してください")
    if not load_name:
        return
    try:
        img = Image.open(load_name).convert("L")
        img2 = img.copy()
        img2.thumbnail((300,300))
        bio = io.BytesIO()
        img2.save(bio, format="PNG")
        window["img"].update(data=bio.getvalue())
        window["txt"].update(load_name)
    except:
        window["img"].update()
        window["txt"].update("失敗しました。")

img = None

def save_image():
    if img == None:
        return
    save_name = sg.popup_get_file("png画像名を付けて保存してください",save_as=True)
    if not save_name:
        sg.PopupTimed("png画像名を入力してください")
        return
    if save_name.endswith(".png") == False:
        save_name = save_name + ".png"
    try:
        img.save(save_name)
        window["txt"].update(save_name + "を保存しました")
    except:
        window["txt"].update("失敗しました。")

while True:
    event, values = window.read()
    if event == "btn1":
        load_image()
    if event == "btn2":
        save_image()
    if event == None:
        break
window.close()

