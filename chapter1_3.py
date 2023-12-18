import tkinter as tk

def label_Change():
    button.configure(text="こんにちは")

root = tk.Tk()
root.geometry("200x150")
root.title("こんにちはテスト")
label = tk.Label(text="")
button = tk.Button(text="実行",command=label_Change)

label.pack()
button.pack()

tk.mainloop()
