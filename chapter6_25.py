import PySimpleGUI as sg
import random

layout = [[sg.Text("私が考えた数を当ててね。1～100までの数だよ")],
          [sg.Image(key="img"),sg.Text(key="txt")],
          [sg.Input(key="in1",size=(10)),sg.Button("入力",key="btn",bind_return_key=True)]]
window = sg.Window("数当てゲーム",layout,font=(None,14),finalize=True)

def question():
    global ans, count,play_flag
    ans = random.randint(1,100)
    count = 0
    window["txt"].update("")
    window["img"].update("futaba0.png")
    play_flag = True

def ans_check():
    global play_flag,count
    if values["in1"].isdecimal() == False:
        window["txt"].update("数字を入れてね")
    else:
        count += 1
        my_num = int(values["in1"])
        if my_num == ans:
            window["txt"].update(f"{count}回目：当たり！\n入力ボタンでまた遊べるよ。")
            window["img"].update("futaba2.png")
            count = 0
            play_flag = False
        elif my_num > ans:
            window["txt"].update(f"{count}回目：もっと小さいよ")
        elif my_num < ans:
            window["txt"].update(f"{count}回目：もっと大きいよ")

question()

while True:
    event, values = window.read()
    if event ==  "btn":
        if play_flag == False:
            question()
        else:
            ans_check()
    if event == None:
        break
window.close()
