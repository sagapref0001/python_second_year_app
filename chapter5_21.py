import PySimpleGUI as sg
import qrcode
import io

sg.theme("DarkBrown3")

layout = [[sg.Text("URL:"),sg.Input(key="in1")],
          [sg.Button("QRコード作成",key="btn1")],
          [sg.Button("ファイルを保存",key="btn2"),sg.Text(key="txt")],
          [sg.Image(key="img")]]
window = sg.Window("QRコードメーカー", layout, size=(320, 420))

img = None
def execute():
    global img
    if not values["in1"]:
        sg.PopupTimed("URLを入力してください")
        return
    img = qrcode.make(values["in1"])
    img.thumbnail((300,300))
    bio = io.BytesIO()
    img.save(bio,format="PNG")
    window["img"].update(data=bio.getvalue())

def save_image():
    if img == None:
        return
    save_name = sg.popup_get_file("png画像名を付けて保存してください",save_as=True)
    if not save_name:
        sg.PopupTimed("pngファイル名を入力してください。")
        return
    if save_name.endswith(".png") == False:
        save_name = save_name + ".png"
    try:
        img.save(save_name)
        window["txt"].update(save_name + "を保存しました。")
    except:
        window["txt"].update("失敗しました。")


while True:
    event, values = window.read()
    if event == "btn1":
        execute()
    if event == "btn2":
        save_image()
    if event == None:
        break
window.close()
