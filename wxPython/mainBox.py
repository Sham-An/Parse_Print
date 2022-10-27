#https://proproprogs.ru/wxpython/standartnye-dialogovye-okna
#https://www.youtube.com/watch?v=90-JemgyMlU&list=PLA0M1Bcd0w8zyJOJXbvTKROHs2JJVGB6C
import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))

        toolbar = self.CreateToolBar()
        br_quit = toolbar.AddTool(wx.ID_ANY, "Выход", wx.Bitmap("images/exit33.png"))
        br_dir = toolbar.AddTool(wx.ID_ANY, "Каталог", wx.Bitmap("images/dir32.png"))
        br_file = toolbar.AddTool(wx.ID_ANY, "Файл", wx.Bitmap("images/file32.png"))
        toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.onQuit, br_quit)
        self.Bind(wx.EVT_TOOL, self.onDir, br_dir)
        self.Bind(wx.EVT_TOOL, self.onOpenFile, br_file)

    def onQuit(self, e):
     #   dlg = wx.MessageBox('Вы дейстительно хотите выйти из программы?', 'Вопрос',
     #                       wx.YES_NO | wx.NO_DEFAULT, self)
        dlg = wx.MessageDialog(self, 'Вы дейстительно хотите выйти из программы?', 'Вопрос',
                            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)

        #dlg.ShowModal()
        res = dlg.ShowModal()

        if res == wx.ID_YES:
            print("Нажата кнопка (да)")
        elif res == wx.ID_NO:
            print("Нажата кнопка (нет)")


    def onDir(self,e):
        """ Select Dir"""
        dlg = wx.DirDialog(self, "Выбор директории...", "D:",
                           wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)

        res = dlg.ShowModal()
        if res == wx.ID_OK:
            print("Выбран каталог: " + dlg.GetPath())

    def OnOpen(self,e):
        """ Open a file"""
        with wx.FileDialog(self, "Open XYZ file", wildcard="XYZ files (*.*)|*.*",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'r') as file:
                    #self.doLoadDataOrWhatever(file)
                    print(file.read())
            except IOError:
                wx.LogError("Cannot open file '%s'." % newfile)


    def onOpenFile(self, e):
        """ Open a file"""
# FileDialog(parent, message=FileSelectorPromptStr,
#            defaultDir="", defaultFile="",
#            wildcard=FileSelectorDefaultWildcardStr, style=FD_DEFAULT_STYLE,
#            pos=DefaultPosition, size=DefaultSize, name=FileDialogNameStr)
        with wx.FileDialog(self, "Открыть файл...", wildcard="Файлы Питона (*.py)|*.py",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            pathname = fileDialog.GetPath()
            print(pathname)


app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()

#https://youtu.be/90-JemgyMlU?list=PLA0M1Bcd0w8zyJOJXbvTKROHs2JJVGB6C&t=419
#wx.TextEntryDialog
# Следующий класс TextEntryDialog представляет диалог для ввода текстового значения. Синтаксис его конструктора следующий:
#
# TextEntryDialog(parent, message, caption=GetTextFromUserPromptStr, value="", style=TextEntryDialogStyle, pos=DefaultPosition)
#
# parent – ссылка на родительское окно (если нет, то None);
# message – сообщение перед строкой ввода;
# caption – заголовок окна;
# value – начальное значение в поле ввода;
# style – стиль окна;
# pos – позиция окна.
# Например, его можно вызвать так:
#
# dlg = wx.TextEntryDialog(self, "Введите имя", "Ввод данных...", "noname")
# res = dlg.ShowModal()
# if res == wx.ID_OK:
#     print(dlg.GetValue())
# Появляется окно с текстом «Введите имя» и начальным значением noname. Остальные параметры берутся по умолчанию. Их возможные значения можно посмотреть в документации на странице:
#
# https://docs.wxpython.org/wx.TextEntryDialog.html
#
# Все ссылки на документацию диалоговых окон приведены под этим видео.
#
# wx.DirDialog
# Следующий класс DirDialog создает диалог для выбора каталога:
#
# DirDialog(parent, message=DirSelectorPromptStr, defaultPath="", style=DD_DEFAULT_STYLE, pos=DefaultPosition, size=DefaultSize, name=DirDialogNameStr)
#
# parent – ссылка на родительское окно (или значение None);
# message – заголовок окна;
# defaultPath – начальный каталог (каталог по умолчанию);
# style – стили окна;
# pos, size – позиция и размер окна.
# Например, его можно вызвать так:
#
# dlg = wx.DirDialog(self, "Выбор директории...", "D:",
#          wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
#
# res = dlg.ShowModal()
# if res == wx.ID_OK:
#     print("Выбран каталог: "+dlg.GetPath())
# Здесь в качестве начального каталога указан диск D. Если записать пустую строку, то будет браться начальный каталог, определяемый ОС. Осталльные параметры, в частности, стили можно посмотреть на странице документации:
#
# https://docs.wxpython.org/wx.DirDialog.html
#
# wx.FileDialog
# С помощью FileDialog создается диалоговое окно для выбора файла. Его синтаксис такой:
#
# FileDialog(parent, message=FileSelectorPromptStr,
#            defaultDir="", defaultFile="",
#            wildcard=FileSelectorDefaultWildcardStr, style=FD_DEFAULT_STYLE,
#            pos=DefaultPosition, size=DefaultSize, name=FileDialogNameStr)
#
# parent – ссылка на родительское окно (или значение None);
# message – заголовок окна;
# defaultDir – стартовая директория;
# defaultFile – файл, выбранный по умолчанию;
# wildcard – селектор для выбора типов файлов;
# style – стилизация окна;
# pos, size – позиция и размер окна.
# Я приведу пример использования данного диалога, взятого из официальной документации:
#
# with wx.FileDialog(self, "Открыть файл...", wildcard="Файлы Питона (*.py)|*.py", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
#       if fileDialog.ShowModal() == wx.ID_CANCEL:
#            return
#
#       pathname = fileDialog.GetPath()
#       print(pathname)
# Здесь используется менеджер контекста, который проверяет: существует ли выбранный файл. И в случае возникновения каких-либо проблем появляется сообщение, что файл не найден. В самом менеджере мы проверяем нажатие на кнопку «Отмена» и если она была нажата, выполняем оператор return и прерываем дальнейшее выполнение обработчика. Иначе, берем путь к файлу и отображаем его в консоли.
#
# Документация по данному диалоговому классу доступна на странице:
#
# https://docs.wxpython.org/wx.FileDialog.html