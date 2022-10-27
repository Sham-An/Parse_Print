import wx

class MainWindow(wx.Frame):
    def __init__(self, parent, title):

        # A "-1" in the size parameter instructs wxWidgets to use the default size.
        # In this case, we select 200px width and the default height.
        wx.Frame.__init__(self, parent, title=title, size=(200,-1))

        # Setting up the menu.
        filemenu= wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open"," Open a file to edit")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Events.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)

        self.Show()

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


app = wx.App(False)
frame = MainWindow(None, "test")
app.MainLoop()