#https://proproprogs.ru/wxpython/shemy-razmeshcheniya-vidzhetov-boxsizer
#https://www.youtube.com/watch?v=4tkvthAC3k8&list=PLA0M1Bcd0w8zyJOJXbvTKROHs2JJVGB6C
import wx

APP_EXIT =1
VIEW_STATUS = 2
VIEW_RGB = 3
VIEW_SRGB = 4

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size= (600,300))

#Мы здесь сначала создаем общий сайзер
        panel = wx.Panel(self)
        #vbox = wx.BoxSizer(wx.HORIZONTAL) #HORIZONTAL default
        vbox = wx.BoxSizer(wx.VERTICAL)
#в котором и будут располагаться все наши виджеты по вертикали. Затем, в первую ячейку вкладываем еще один сайзер
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

#В первую ячейку помещаем обычный текст «Путь к файлу» с отступом справа 8 пикселей,
        # а во вторую – поле ввода:
        st1 = wx.StaticText(panel, label='Путь к файлу:')
        tc = wx.TextCtrl(panel)

        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        hbox1.Add(tc, proportion=1) #proportion=1 растяжение поля по горизонтали на макс. длину. Default= 0.
        #После формирования сайзера hbox1 добавляем его в сайзер vbox:
        #Устанавливаем флаг EXPAND и отступы по 10 пикселей слева, справа и сверху.
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

# В следующую ячейку сайзера vbox помещаем текст «Содержимое файла»,
        # отступы со всех сторон по 10 пикселей:
        st2 = wx.StaticText(panel, label='Содержимое файла')
        vbox.Add(st2, flag=wx.EXPAND | wx.ALL, border=10)

#По аналогии, ниже размещаем многострочное поле ввода:
        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        vbox.Add(tc2, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, border=10)
#И в конце размещаем две кнопки:
        btnOk = wx.Button(panel, label='Да', size=(70, 30))
        btnCn = wx.Button(panel, label='Отмена', size=(70, 30))
#в еще одном вложенном горизонтальном сайзере с отступами слева 10 пикселей:
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(btnOk, flag=wx.LEFT, border=10)
        hbox2.Add(btnCn, flag=wx.LEFT, border=10)
#Размещаем его в основном блоке,
        # выравнивая по правому краю и с отступами справа и снизу по 10 пикселей:
        vbox.Add(hbox2, flag=wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT, border=10)
        panel.SetSizer(vbox)
#изменим размер шрифта в нашем интерфейсе. Для этого запишем такие строчки:
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetPointSize(12)
        panel.SetFont(font)
        #img1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("images/js.png"))
        #img2 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("images/python.png"))

        #img1 = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap("images/js.png"))
        #img2 = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap("images/python.png"))

        #img1.SetPosition((30, 30))
        #img2.SetPosition((300, 50))


        #mp = wx.Panel(panel) #создадим виджет в виде панели и расположим его по центру нашего окна:
        #mp.SetBackgroundColour('#FFFFE5')
        #vbox.Add(mp, wx.ID_ANY, wx.EXPAND | wx.ALL, 20) #

        #vbox.Add(img1, wx.ID_ANY, wx.EXPAND) #wx.EXPAND растянуть изображение
        #vbox.Add(img2, wx.ID_ANY, wx.EXPAND)



        #self.SetSizer(vbox)
        panel.SetSizer(vbox)

    #     menubar = wx.MenuBar()
    #     fileMenu = wx.Menu()
    #     expMenu = wx.Menu()
    #
    #     fileMenu.Append(wx.ID_NEW, '&Новый\tCtrl+N')
    #     fileMenu.Append(wx.ID_OPEN, '&Открыть\tCtrl+O')
    #     fileMenu.Append(wx.ID_SAVE, '&Сохранить\tCtrl+S')
    #     fileMenu.AppendSubMenu(expMenu, "&Экспорт")
    #
    #     fileMenu.AppendSeparator()
    #     # item = wx.MenuItem(fileMenu, wx.ID_EXIT, "Выход", "Выход из приложения")
    #     # fileMenu.Append(item)
    #
    #     item = fileMenu.Append(APP_EXIT, "Выход\tCtrl+Q", "Выход из приложения")
    #     menubar.Append(fileMenu, "&File")
    #
    #     viewMenu = wx.Menu()
    #     self.vStatus =viewMenu.Append(VIEW_STATUS, 'Статустная строка', kind=wx.ITEM_CHECK)
    #     self.vRgb = viewMenu.Append(VIEW_RGB, 'Тип RGB', 'Тип RGB', kind=wx.ITEM_RADIO)
    #     self.vSrgb = viewMenu.Append(VIEW_SRGB, 'Тип sRGB', 'Тип sRGB', kind=wx.ITEM_RADIO)
    #     menubar.Append(viewMenu, "&Вид")
    #
    #     self.SetMenuBar(menubar)
    #
    #     self.Bind(wx.EVT_MENU, self.onQuit, id=APP_EXIT)
    #     # self.vStatus = viewMenu.Append(VIEW_STATUS, 'Статустная строка', kind=wx.ITEM_CHECK)
    #     # self.vRgb = viewMenu.Append(VIEW_RGB, 'Тип RGB', 'Тип RGB', kind=wx.ITEM_RADIO)
    #     # self.vSrgb = viewMenu.Append(VIEW_SRGB, 'Тип sRGB', 'Тип sRGB', kind=wx.ITEM_RADIO)
    #     self.Bind(wx.EVT_MENU, self.onStatus, id=VIEW_STATUS)
    #     self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_RGB)
    #     self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_SRGB)
    #
    # def onStatus(self, event):
    #     if self.vStatus.IsChecked():
    #         print("Показать статусную строку")
    #     else:
    #         print("Скрыть статусную строку")
    #
    # def onImageType(self, event):
    #     if self.vRgb.IsChecked():
    #         print("Режим RGB")
    #     elif self.vSrgb.IsChecked():
    #         print("Режим sRGB")
    #
    # def onQuit(self, event):
    #     self.Close()
    #

app = wx.App()

wnd = MyFrame(None, "Hello World!")
wnd.Show()
app.MainLoop()
