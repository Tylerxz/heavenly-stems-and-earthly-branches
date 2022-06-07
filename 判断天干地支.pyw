from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.Widgets()

    def Widgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='判断天干地支', command=self.judge)
        self.alertButton.pack()

    def judge(self):
        y = int(self.nameInput.get())
        s1="庚辛壬癸甲乙丙丁戊己"
        s2="申酉戌亥子丑寅卯辰巳午未"
        a=s1[y%10]
        b=s2[y%12]
        c=a+b
        messagebox.showinfo('结果', c)

app = Application()
# 设置窗口标题:
app.master.title('请输入年份')
# 主消息循环:
app.mainloop()
