import wx


class MyTextCtrl(wx.TextCtrl):
    def set_value(self, value):
        if isinstance(value, (int, float)):
            value = str(value)
        self.SetValue(value)