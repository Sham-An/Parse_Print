#https://proproprogs.ru/wxpython/vidy-sayzerov
#https://www.youtube.com/watch?v=7ehPJFL90mc&list=PLA0M1Bcd0w8zyJOJXbvTKROHs2JJVGB6C
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, -1, title)


app = wx.App()

wnd = MyFrame(None, "Hello World!")
wnd.Show()
app.MainLoop()
