import wx


class MyTextCtrl(wx.TextCtrl):
    def set_value(self, value):
        if isinstance(value, int):
            value = str(value)
        self.SetValue(value)