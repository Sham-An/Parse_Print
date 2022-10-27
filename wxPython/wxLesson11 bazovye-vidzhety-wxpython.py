#https://proproprogs.ru/wxpython/bazovye-vidzhety-wxpython
#https://www.youtube.com/watch?v=ntrk7aeqcJE&list=PLA0M1Bcd0w8zyJOJXbvTKROHs2JJVGB6C
import wx

APP_EXIT =1
VIEW_STATUS = 2
VIEW_RGB = 3
VIEW_SRGB = 4

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, -1, title)

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        expMenu = wx.Menu()

        fileMenu.Append(wx.ID_NEW, '&Новый\tCtrl+N')
        fileMenu.Append(wx.ID_OPEN, '&Открыть\tCtrl+O')
        fileMenu.Append(wx.ID_SAVE, '&Сохранить\tCtrl+S')
        fileMenu.AppendSubMenu(expMenu, "&Экспорт")

        fileMenu.AppendSeparator()
        # item = wx.MenuItem(fileMenu, wx.ID_EXIT, "Выход", "Выход из приложения")
        # fileMenu.Append(item)

        item = fileMenu.Append(APP_EXIT, "Выход\tCtrl+Q", "Выход из приложения")
        menubar.Append(fileMenu, "&File")

        viewMenu = wx.Menu()
        self.vStatus =viewMenu.Append(VIEW_STATUS, 'Статустная строка', kind=wx.ITEM_CHECK)
        self.vRgb = viewMenu.Append(VIEW_RGB, 'Тип RGB', 'Тип RGB', kind=wx.ITEM_RADIO)
        self.vSrgb = viewMenu.Append(VIEW_SRGB, 'Тип sRGB', 'Тип sRGB', kind=wx.ITEM_RADIO)
        menubar.Append(viewMenu, "&Вид")

        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.onQuit, id=APP_EXIT)
        # self.vStatus = viewMenu.Append(VIEW_STATUS, 'Статустная строка', kind=wx.ITEM_CHECK)
        # self.vRgb = viewMenu.Append(VIEW_RGB, 'Тип RGB', 'Тип RGB', kind=wx.ITEM_RADIO)
        # self.vSrgb = viewMenu.Append(VIEW_SRGB, 'Тип sRGB', 'Тип sRGB', kind=wx.ITEM_RADIO)
        self.Bind(wx.EVT_MENU, self.onStatus, id=VIEW_STATUS)
        self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_RGB)
        self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_SRGB)

    def onStatus(self, event):
        if self.vStatus.IsChecked():
            print("Показать статусную строку")
        else:
            print("Скрыть статусную строку")

    def onImageType(self, event):
        if self.vRgb.IsChecked():
            print("Режим RGB")
        elif self.vSrgb.IsChecked():
            print("Режим sRGB")

    def onQuit(self, event):
        self.Close()


app = wx.App()

wnd = MyFrame(None, "Hello World!")
wnd.Show()
app.MainLoop()
