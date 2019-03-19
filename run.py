import wx

from ui import MainFrame


class UI(wx.App):
    def OnInit(self):
        # 初始化UI
        MainFrame(title='维修记录单管理软件', size=(1250, 770))
        self.MainLoop()


if __name__=='__main__':
    UI()