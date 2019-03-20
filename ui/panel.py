import wx.lib.scrolledpanel


class MyPanel(wx.lib.scrolledpanel.ScrolledPanel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)
        self.SetupScrolling()