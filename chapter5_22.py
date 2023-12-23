import PySimpleGUI as sg
import random

kuji = ["大吉","中吉","小吉","吉","凶","大凶"]
kekka = random.choice(kuji)
print(kekka)

layout = [[sg.Text("さあ、おみくじをひきましょう！")],
          [sg.Image("futaba0.png")],
          [sg.Text(key="txt1")],
          [sg.Button("おみくじをひく",key="btn")]]
window = sg.Window("おみくじアプリ",layout,size=(400,200))

def execute():
    kuji = ["大吉", "中吉", "小吉", "吉", "凶", "大凶"]
    txt = random.choice(kuji)
    window["txt1"].update("結果は" + txt + "でした！")



while True:
    event, values = window.read()
    if event == "btn":
        execute()
    if event == None:
        break
window.close()


