import PySimpleGUI as sg
import datetime
sg.theme("DarkBrown3")

layout = [[sg.Text("00:00:00", font=("Arial",24), key="txt1")],
          [sg.ML(font=("Arial",18),size=(40,12),key="txt2")]]

window = sg.Window("時間割アプリ",layout,font=(None,14),size=(500,300),keep_on_top="True")

sch = [["1時限",8,50],
       ["2時限",10,30],
       ["昼休み",12,40],
       ["3時限",13,20],
       ["4時限",15,10],
       ["5時限",17,00],
       ["6時限",18,50]]

def execute():
    now = datetime.datetime.now()
    now = now.replace(hour=10)
    window["txt1"].update(f"{now:%H:%M:%S}")
    txt2 = ""
    for s in sch:
        dt = now.replace(hour=s[1],minute=s[2],second=0) - now
        if dt.total_seconds() > 0:
            txt2 += f"{s[0]}【{s[1]:02d}:{s[2]:02d}】あと{dt}です。\n"
        else:
            txt2 += f"{s[0]}【{s[1]:02d}:{s[2]:02d}】---\n"
    window["txt2"].update(txt2)

while True:
    event, values = window.read(timeout=500)
    if event == None:
        break
    execute()
window.close()


