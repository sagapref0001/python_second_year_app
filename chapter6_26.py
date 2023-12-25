import PySimpleGUI as sg
import random

layout = [[sg.Text("31ゲームをしよう！　31を言うと負けだよ")],
          [sg.Image(key="img"),sg.Text(key="txt1")],
          [sg.Text(key="txt2")],
          [sg.Input("1",key="in1",font=(None,14),size=(10)),sg.Button("入力",key="btn1",bind_return_key=True)]]
window = sg.Window("31ゲーム",layout,font=(None,14),finalize=True)

play_flag = 0

def get_next_num(n):
    global next_num, choice_msg
    next_num = list(range(n+1,min(32,n+4)))
    choice_msg = f"{next_num}から入力してください。"
    window["txt2"].update(choice_msg)


def question():
    global play_flag
    get_next_num(0)
    window["txt1"].update("さあ、ゲームを始めるよ")
    window["img"].update("futaba0.png")
    play_flag= True

def comp_turn(com_num):
    win_num = [2,6,10,14,18,22,26,30]
    get_next_num(com_num)
    com_num += 1
    for n in next_num:
        if n in win_num:
            com_num = n
    if random.randint(0,1) > 0:
        com_num = next_num[0]
    window["txt1"].update(f"私は、{com_num}にするよ。")
    get_next_num(com_num)

def my_turn():
    global play_flag
    if values["in1"].isdecimal == False:
        window["txt1"].update("数字を入力してね")
    else:
        my_num = int(values["in1"])
        if my_num  in next_num:
            if my_num == 31:
                window["txt1"].update("31って言ったね。\nあなたの負けです。")
                window["img"].update("futaba2.png")
                window["txt2"].update("入力ボタンを押すとまた遊べるよ。")
                play_flag = False
            elif my_num == 30:
                window["txt2"].update("31。あなたの勝ちです。\nおめでとう")
                window["img"].update("futaba1.png")
                window["txt2"].update("入力ボタンを押すとまた遊べるよ。")
                play_flag = False
            else:
                comp_turn(my_num)
        else:
            window["txt1"].update(choice_msg)

question()
while True:
    event, values = window.read()
    if event == "btn1":
        if play_flag == False:
            question()
        else:
            my_turn()
    if event == None:
        break
window.close()