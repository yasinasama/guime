import wx

from ui import MainFrame


class UI(wx.App):
    def __init__(self):
        super(UI, self).__init__()

        MainFrame(title='维修记录单管理软件', size=(1200, 800))
        self.MainLoop()


if __name__=='__main__':
    UI()