import wx
import wx.grid


class MyGrid(wx.grid.Grid):
    def __init__(self, parent):
        super(MyGrid, self).__init__(parent=parent)

    def set_cell_value(self, row, col, value):
        if isinstance(value, int):
            value = str(value)
        self.SetCellValue(row, col, value)

