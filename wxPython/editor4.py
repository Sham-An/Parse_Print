import wx
import os


class Window(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(300, 250))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)

        menu = wx.Menu()
        openItem = menu.Append(wx.ID_OPEN, "Open", "Push the button to open the file")
        aboutItem = menu.Append(wx.ID_ABOUT, "About", "Push the button to get an information about this application")
        exitItem = menu.Append(wx.ID_EXIT, "Exit", "Push the button to leave this application")
        bar = wx.MenuBar()
        bar.Append(menu, "File")
        self.SetMenuBar(bar)
        self.Bind(wx.EVT_MENU, self.OnOpen, openItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)

    def OnOpen(self, event):

        # if self.contentNotSaved:
        #     if wx.MessageBox("Current content has not been saved! Proceed?", "Please confirm",
        #                      wx.ICON_QUESTION | wx.YES_NO, self) == wx.NO:
        #         return

        # otherwise ask the user what new file to open
        with wx.FileDialog(self, "Open XYZ file", wildcard="files (*.*)|*.*",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
#wildcard = "BMP and GIF files (*.bmp;*.gif)|*.bmp;*.gif|PNG files (*.png)|*.png"
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'r') as file:
                    #self.doLoadDataOrWhatever(file)
                    print(file.read())
            except IOError:
                wx.LogError("Cannot open file '%s'." % newfile)


    # def OnOpen(self, e):
    #     self.dirname = " "
    #     openDlg = wx.FileDialog(self, "Choose a file to open", self.dirname, " ", "*.*", wx.OPEN)
    #     if openDlg.ShowModal() == wx.ID_OK:
    #         self.filename = openDlg.GetFilename()
    #         self.dirname = openDlg.GetDirectory()
    #         f = open(os.path.join(self.dirname, self.filename), "r")
    #         self.control.SetValue(f.read())
    #         f.close()
    #         wnd.SetTitle(self.filename + " - pyNote")

    def OnAbout(self, e):
        aboutDlg = wx.MessageDialog(self, "This is a mini editor keeping your text", "About pyNote", wx.OK)
        aboutDlg.ShowModal()

    def OnExit(self, e):
        self.control.SetValue("Close me, please! :(")


app = wx.App()
wnd = Window(None, "pyNote")
app.MainLoop()
