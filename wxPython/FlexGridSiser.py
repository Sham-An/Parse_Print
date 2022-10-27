#https://proproprogs.ru/wxpython/vidy-sayzerov
#
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, -1, title)

        panel = wx.Panel(self)
        #vbox = wx.BoxSizer(wx.HORIZONTAL) #HORIZONTAL default
        vbox = wx.BoxSizer(wx.VERTICAL)

# Но нам нужны еще отступы от границ окна.
# Для этого мы поместим сайзер fb в другой сайзер BoxSizer
# и уже в нем укажем необходимые отступы:
        hbox = wx.BoxSizer()

        #Для начала создадим такой сайзер с 4 строками, 2 столбцами и расстояниями между ячейками 10 пикселей:
        fb = wx.FlexGridSizer(4, 2, 10, 10)
#Далее, используя уже знакомый метод AddMany() добавим все виджеты в данный объект:
        fb.AddMany([ (wx.StaticText(panel, label="Ф.И.О.:")),
                 (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                 (wx.StaticText(panel, label="email:")),
                 (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                 (wx.StaticText(panel, label="Адрес:")),
                 (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                 (wx.StaticText(panel, label="О себе:")),
                 (wx.TextCtrl(panel, style=wx.NB_MULTILINE), wx.ID_ANY, wx.EXPAND)
               ])
#И свяжем панель с этим сайзером:
        #panel.SetSizer(fb)
# укажем, что второй столбец следует расширять по максимуму. Воспользуемся методом:
        #AddGrowableCol(self, col, proportion=0)
        fb.AddGrowableCol(1, 1)
#Далее, вот этот последний элемент с текстом «О себе» следует расширить до нижней границы окна. Это можно сделать с помощью похожего метода:
#AddGrowableRow(self, row, proportion=0) #и для row=3 укажем proportion=1:
        fb.AddGrowableRow(3, 1)
# Но нам нужны еще отступы от границ окна. # Для этого мы поместим сайзер fb в другой сайзер BoxSizer
# и уже в нем укажем необходимые отступы:
        #hbox = wx.BoxSizer()
        hbox.Add(fb, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
#Свяжем панель с этим новым объектом:
        panel.SetSizer(hbox)


app = wx.App()

wnd = MyFrame(None, "Hello World!")
wnd.Show()
app.MainLoop()
