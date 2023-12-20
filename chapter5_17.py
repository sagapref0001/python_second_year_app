from pathlib import Path

def savetext(filename):
    p = Path(filename)
    txt = "書き出し用のテスト用テキストデータです。"
    p.write_text(txt,encoding="utf-8")

savetext("output")