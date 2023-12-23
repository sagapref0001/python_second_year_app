import PySimpleGUI as sg
import random

layout = [[sg.Text("足し算ゲームです。問題の答えを入力してね。",key="txt0")],
          [sg.Image(key="img"),sg.T(key="txt1")],
          [sg.Text(key="txt2",size=(20)),sg.Input("",key="in1",size=(10)),sg.Button("入力",key="btn1",bind_return_key=True)]]
window = sg.Window("足し算ゲーム",layout, font=(None,14),finalize=True,)

result = 0
play_flag = None
def question():
    global result, play_flag
    num1 = random.randint(0,100)
    num2 = random.randint(0,100)
    result = num1 + num2
    window["txt1"].update("")
    window["txt2"].update(f"問題: {num1} + {num2} =?")
    window["img"].update("futaba0.png")
    play_flag = True

def ans_check():
    global play_flag
    if values["in1"].isdecimal() == False:
        window["txt1"].update("数字を入力してね。")
    else:
        my_num = int(values["in1"])
        if my_num == result:
            window["txt1"].update("正解です。")
            window["txt0"].update("入力ボタンを押すと、次の問題が出るよ")
            window["img"].update("futaba1.png")
            play_flag = False
        else:
            window["txt1"].update("まちがいです。")
            window["img"].update("futaba2.png")


question()
while True:
    event, values = window.read()
    if event == "btn1":
        if  play_flag == False:
            question()
        else:
            ans_check()
    if event == None:
        break
window.close()