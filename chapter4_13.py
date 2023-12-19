import datetime

now = datetime.datetime.now()
print(f"{now:%H時%M分%S秒}")
print(f"{now:%H:%M:%S}")
print(f"{now:%p %I %M %S}")
print(f"{now:%Y/%m/%d(%a)}")

start = datetime.datetime.now()
goal = now.replace(hour=20,minute=30,second=0)
input("Enterキーを押してください")
now = datetime.datetime.now()
td = goal - now
print(td)
