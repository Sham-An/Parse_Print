#https://proproprogs.ru/wxpython/sobstvennye-dialogovye-okna-klass-dialog
#https://www.youtube.com/watch?v=YLJmdxjI5GU&list=PLA0M1Bcd0w8zyJOJXbvTKROHs2JJVGB6C
import wx

APP_EXIT =1
VIEW_STATUS = 2
VIEW_RGB = 3
VIEW_SRGB = 4

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, -1, title)


app = wx.App()

wnd = MyFrame(None, "Hello World!")
wnd.Show()
app.MainLoop()
