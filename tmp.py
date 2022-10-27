import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, size=(400, 200))
        fileMenu = wx.Menu()
        openItem = fileMenu.Append(wx.ID_OPEN, "&Open", " Open a file to edit")
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.OnOpen, openItem)

    def OnOpen(self, event):
        # otherwise ask the user what new file to open
        with wx.FileDialog(self, "Open XYZ file", wildcard="XYZ files (*.*)|*.*",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'r') as file:
                    # self.doLoadDataOrWhatever(file)
                    print(file.read())  # see, it works!
            except IOError:
                wx.LogError("Cannot open file '%s'." % newfile)


app = wx.App()
frame = MyFrame(None, wx.ID_ANY, "test")
frame.Show()
app.MainLoop()
