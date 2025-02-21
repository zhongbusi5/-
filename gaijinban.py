import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox

def qd1():
    name = xm0.get()
    gender = xb0.get()
    nation = mz0.get()
    id_number = sfz0.get()
    phone = dh0.get()
    wechat_qq = wxqq0.get()
    intro = grjj0.get("1.0", tk.END)
    messagebox.showinfo("提示", "录入完成")
    root.destroy()

    print("姓名:", name)
    print("性别:", gender)
    print("民族:", nation)
    print("身份证号:", id_number)
    print("电话号:", phone)
    print("微信/QQ:", wechat_qq)
    print("个人简介:", intro.strip())

def qx1():
    root.destroy()

root = tk.Tk()
root.geometry('500x300+500+200')
root.title('身份信息')

xm = tk.Label(root, text='姓名：')
xm.place(x=80, y=30)
xm0= tk.Entry(root, width=15)
xm0.place(x=120, y=30)

xb = tk.Label(root, text='性别：')
xb.place(x=80, y=50)
xb0 = tk.Entry(root, width=15)
xb0.place(x=120, y=50)

mz = tk.Label(root, text='民族：')
mz.place(x=80, y=70)
mz0= tk.Entry(root, width=15)
mz0.place(x=120, y=70)

sfz = tk.Label(root, text='身份证号：')
sfz.place(x=240, y=30)
sfz0 = tk.Entry(root, width=15)
sfz0.place(x=300, y=30)

dh = tk.Label(root, text='电话号：')
dh.place(x=240, y=50)
dh0 = tk.Entry(root, width=15)
dh0.place(x=300, y=50)

wxqq = tk.Label(root, text='微信/QQ：')
wxqq.place(x=240, y=70)
wxqq0 = tk.Entry(root, width=15)
wxqq0.place(x=300, y=70)

grjj = tk.Label(root, text='个人简介：')
grjj.place(x=140, y=180)
grjj0 = tk.Text(root, height=8, width=25)
grjj0.place(x=200, y=180)

qd0 = tk.Button(root,text='确定', command=qd1)
qd0.place(x=50, y=150)

qx0 = tk.Button(root, text='取消', command=qx1)
qx0.place(x=100, y=150)

root.mainloop()
