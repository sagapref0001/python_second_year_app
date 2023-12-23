import PySimpleGUI as sg
import random

layout = [[sg.Text("私とじゃんけんをしよう")],
          [sg.Image("futaba0.png",key="img1"),sg.Image(key="img2")],
          [sg.Text(key="txt1")],
          [sg.Button("グー",key="btn1"),sg.Button("チョキ",key="btn2"),sg.Button("パー",key="btn3")]]
window = sg.Window("じゃんけんアプリ", layout, font=(None,14), size=(400,400))

def execute(my_num):
    janken = ["h0.png","h1.png","h2.png"]
    face = ["futaba0.png","futaba1.png","futaba2.png"]
    winner = ["あなたの勝ちです。","あいこです。","コンピューターの勝ちです。"]
    comp = random.randint(0,2)
    result = (comp - my_num) % 3
    window["img1"].update(face[(comp - my_num) % 3])
    window["img2"].update(janken[comp])
    window["txt1"].update("じゃんけんの結果は" + winner[result])


while True:
    event, value = window.read()
    if event == "btn1":
        execute(0)
    if event == "btn2":
        execute(1)
    if event == "btn3":
        execute(2)
    if event == None:
        break

window.close()

