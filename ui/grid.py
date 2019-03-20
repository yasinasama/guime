import wx.grid


class MyGrid(wx.grid.Grid):
    def __init__(self, parent):
        super(MyGrid, self).__init__(parent=parent)

    def set_cell_value(self, row, col, value):
        if isinstance(value, (int, float)):
            value = str(value)
        self.SetCellValue(row, col, value)

    def get_selected_rows(self):
        if self.GetSelectedRows():
            return self.GetSelectedRows()
        if self.GetSelectedCells():
            return [row[0] for row in self.GetSelectedCells()]
        if self.GetSelectionBlockTopLeft():
            top_row = self.GetSelectionBlockTopLeft()[0][0]
            bottom_row = self.GetSelectionBlockBottomRight()[0][0]
            return list(range(top_row, bottom_row+1))
        return [self.GetGridCursorRow()]

