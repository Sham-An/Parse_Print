#https://proproprogs.ru/wxpython/mehanizm-obrabotki-sobytiy
#https://www.youtube.com/watch?v=DdHMnHeX5rY&list=PLA0M1Bcd0w8zyJOJXbvTKROHs2JJVGB6C
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title = title, size = (600, 300))

        btn1 = wx.Button(self, wx.ID_ANY, "Кнопка 1")
        btn2 = wx.Button(self, wx.ID_ANY, "Кнопка 2")
        btn1.SetPosition(wx.Point(10, 10))
        btn2.SetPosition(wx.Point(200, 10))

        #self.Bind(wx.EVT_LEFT_DOWN, self.onLeftDown)
        self.Bind(wx.EVT_BUTTON, self.onButton1, id=btn1.GetId())
        self.Bind(wx.EVT_BUTTON, self.onButton2, id=btn2.GetId())


    def onLeftDown(self, event):
        print("Левая кнопка нажата")

    def onButton1(self, event):
        print("Первая кнопка нажата")

    def onButton2(self, event):
        print("Вторая кнопка нажата")

app = wx.App()

wnd = MyFrame(None, "Hello World!")
wnd.Show()
app.MainLoop()
