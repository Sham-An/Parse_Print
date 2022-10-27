# gifviewer.py

import os
import wx
import wx.animate


class frameMain(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, id=wx.ID_ANY, title=u"My Gif Viewer", pos=wx.DefaultPosition,
                          size=wx.Size(655, 622), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.Size(655, -1), wx.DefaultSize)

        bSizerFrame = wx.BoxSizer(wx.VERTICAL)

        self.panelMain = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizerPanel = wx.BoxSizer(wx.VERTICAL)

        bSizerPanelMain = wx.BoxSizer(wx.VERTICAL)

        bSizerDir = wx.BoxSizer(wx.VERTICAL)

        bSizerDirHor = wx.BoxSizer(wx.HORIZONTAL)

        sbSizerDir = wx.StaticBoxSizer(wx.StaticBox(self.panelMain, wx.ID_ANY, u"GIF Directory"), wx.VERTICAL)

        self.dirPickerDir = wx.DirPickerCtrl(self.panelMain, wx.ID_ANY, wx.EmptyString, u"Select a folder",
                                             wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        sbSizerDir.Add(self.dirPickerDir, 1, wx.ALL | wx.EXPAND, 5)

        bSizerDirHor.Add(sbSizerDir, 1, wx.ALL | wx.EXPAND, 10)

        bSizerDir.Add(bSizerDirHor, 1, wx.EXPAND, 0)

        bSizerPanelMain.Add(bSizerDir, 0, wx.EXPAND, 0)

        bSizerSplit = wx.BoxSizer(wx.VERTICAL)

        bSizerSplitHor = wx.BoxSizer(wx.HORIZONTAL)

        bSizerListbox = wx.BoxSizer(wx.HORIZONTAL)

        bSizerGifile = wx.BoxSizer(wx.VERTICAL)

        listBoxGifilesChoices = []
        self.listBoxGifiles = wx.ListBox(self.panelMain, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, -1),
                                         listBoxGifilesChoices, 0)
        bSizerGifile.Add(self.listBoxGifiles, 1, wx.ALL, 10)

        bSizerListbox.Add(bSizerGifile, 1, wx.EXPAND, 0)

        bSizerSplitHor.Add(bSizerListbox, 0, wx.EXPAND, 0)

        bSizerView = wx.BoxSizer(wx.HORIZONTAL)

        bSizerViewHor = wx.BoxSizer(wx.HORIZONTAL)

        self.animCtrlGifs = wx.animate.AnimationCtrl(self.panelMain, wx.ID_ANY, wx.animate.NullAnimation,
                                                     wx.DefaultPosition, wx.DefaultSize, wx.animate.AC_DEFAULT_STYLE)
        bSizerViewHor.Add(self.animCtrlGifs, 1, wx.ALL | wx.EXPAND, 10)

        bSizerView.Add(bSizerViewHor, 1, wx.EXPAND, 0)

        bSizerSplitHor.Add(bSizerView, 1, wx.EXPAND, 0)

        bSizerSplit.Add(bSizerSplitHor, 1, wx.EXPAND, 0)

        bSizerPanelMain.Add(bSizerSplit, 1, wx.EXPAND, 0)

        bSizerPanel.Add(bSizerPanelMain, 1, wx.EXPAND, 0)

        self.panelMain.SetSizer(bSizerPanel)
        self.panelMain.Layout()
        bSizerPanel.Fit(self.panelMain)
        bSizerFrame.Add(self.panelMain, 1, wx.EXPAND, 0)

        self.SetSizer(bSizerFrame)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.dirPickerDir.Bind(wx.EVT_DIRPICKER_CHANGED, self.dirPickerDirOnDirChanged)
        self.listBoxGifiles.Bind(wx.EVT_LISTBOX, self.listBoxGifilesOnListBox)

        # ------------ Add widget program settings
        self.GifPath = None

        # ------------ Call Populates

        self.Show()

        # ------------ Event handlers

    def dirPickerDirOnDirChanged(self, event):
        self.GifPath = event.GetPath()
        self.popGifList()

    def popGifList(self):
        self.listBoxGifiles.Clear()
        allFiles = os.listdir(self.GifPath)
        for file in allFiles:
            if file.endswith('.gif'):
                self.listBoxGifiles.Append(file)

    def listBoxGifilesOnListBox(self, event):
        try:
            selGif = event.GetString()
            gifile = os.path.join(self.GifPath, selGif)
            self.animCtrlGifs.LoadFile(gifile, type=wx.animate.ANIMATION_TYPE_ANY)
            self.animCtrlGifs.Play()
        except:
            print
            "Listbox error"


if __name__ == "__main__":
    app = wx.App(False)
    frame = frameMain()
    app.MainLoop()