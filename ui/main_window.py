import math
import traceback

import wx
import wx.grid

from db import DB_CONN

from .child_window import ChildFrame
from .grid import MyGrid
from .textctrl import MyTextCtrl
from .panel import MyPanel


class MainFrame(wx.Frame):
    def __init__(self, title, size):
        super(MainFrame, self).__init__(parent=None, title=title, size=size)

        MainPanel(self)

        self.Centre()
        self.Show()


class MainPanel(MyPanel):
    def __init__(self, parent):
        super(MainPanel, self).__init__(parent=parent)

        self._create()

    def _create(self):
        main_box = wx.GridBagSizer()

        st1 = wx.StaticText(self, label='结算单号', style=wx.ALIGN_RIGHT, size=(100, 25))
        st2 = wx.StaticText(self, label='开单日期', style=wx.ALIGN_RIGHT, size=(100, 25))
        st3 = wx.StaticText(self, label='结算日期', style=wx.ALIGN_RIGHT, size=(100, 25))
        st4 = wx.StaticText(self, label='车架号码', style=wx.ALIGN_RIGHT, size=(100, 25))
        st5 = wx.StaticText(self, label='车牌号码', style=wx.ALIGN_RIGHT, size=(100, 25))
        st6 = wx.StaticText(self, label='车辆类型', style=wx.ALIGN_RIGHT, size=(100, 25))
        st7 = wx.StaticText(self, label='本次里程', style=wx.ALIGN_RIGHT, size=(100, 25))
        st8 = wx.StaticText(self, label='车主姓名', style=wx.ALIGN_RIGHT, size=(100, 25))
        st9 = wx.StaticText(self, label='联系电话', style=wx.ALIGN_RIGHT, size=(100, 25))
        st10 = wx.StaticText(self, label='合计金额', style=wx.ALIGN_RIGHT, size=(100, 25))
        st11 = wx.StaticText(self, label='备注信息', style=wx.ALIGN_RIGHT, size=(100, 25))
        st12 = wx.StaticText(self, label='保险公司', style=wx.ALIGN_RIGHT, size=(100, 25))
        st13 = wx.StaticText(self, label='保险到期', style=wx.ALIGN_RIGHT, size=(100, 25))

        self.st20 = wx.StaticText(self, label='0/0', style=wx.ALIGN_CENTER, size=(100, 25))

        self.tc1 = MyTextCtrl(self, style=wx.TE_PROCESS_ENTER, size=(100, 25))
        self.tc2 = MyTextCtrl(self, style=wx.TE_PROCESS_ENTER, size=(100, 25))
        self.tc3 = MyTextCtrl(self, style=wx.TE_PROCESS_ENTER, size=(100, 25))
        self.tc4 = MyTextCtrl(self, style=wx.TE_PROCESS_ENTER, size=(220, 25))
        self.tc5 = MyTextCtrl(self, style=wx.TE_PROCESS_ENTER, size=(100, 25))
        self.tc6 = MyTextCtrl(self, style=wx.TE_PROCESS_ENTER, size=(100, 25))
        self.tc7 = MyTextCtrl(self, style=wx.TE_PROCESS_ENTER, size=(100, 25))
        self.tc8 = MyTextCtrl(self, style=wx.TE_PROCESS_ENTER, size=(100, 25))
        self.tc9 = MyTextCtrl(self, style=wx.TE_PROCESS_ENTER, size=(100, 25))
        self.tc10 = MyTextCtrl(self, style=wx.TE_PROCESS_ENTER, size=(100, 25))
        self.tc11 = MyTextCtrl(self, style=wx.TE_PROCESS_ENTER | wx.TE_MULTILINE, size=(220, 70))
        self.tc12 = MyTextCtrl(self, style=wx.TE_PROCESS_ENTER, size=(100, 25))
        self.tc13 = MyTextCtrl(self, style=wx.TE_PROCESS_ENTER, size=(100, 25))

        btn1 = wx.Button(self, label='新建')
        btn2 = wx.Button(self, label='查询')
        btn3 = wx.Button(self, label='删除')
        btn4 = wx.Button(self, label='上一页')
        btn5 = wx.Button(self, label='下一页')

        self.table = MainGrid(self)

        main_box.Add(st1, pos=(1, 0), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st2, pos=(1, 2), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st3, pos=(1, 4), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st4, pos=(1, 8), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st5, pos=(2, 0), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st6, pos=(2, 2), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st7, pos=(2, 4), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st8, pos=(3, 0), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st9, pos=(3, 2), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st10, pos=(3, 4), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st11, pos=(2, 8), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st12, pos=(1, 6), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st13, pos=(2, 6), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)

        main_box.Add(self.st20, pos=(25, 1), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)

        main_box.Add(self.tc1, pos=(1, 1), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc2, pos=(1, 3), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc3, pos=(1, 5), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc4, pos=(1, 9), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc5, pos=(2, 1), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc6, pos=(2, 3), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc7, pos=(2, 5), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc8, pos=(3, 1), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc9, pos=(3, 3), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc10, pos=(3, 5), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc11, pos=(2, 9), span=(2, 1), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc12, pos=(1, 7), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc13, pos=(2, 7), flag=wx.TOP | wx.BOTTOM, border=10)

        main_box.Add(btn1, pos=(0, 0), flag=wx.TOP | wx.LEFT, border=10)
        main_box.Add(btn2, pos=(0, 1), flag=wx.TOP, border=10)
        main_box.Add(btn3, pos=(0, 2), flag=wx.TOP, border=10)
        main_box.Add(btn4, pos=(25, 0), flag=wx.TOP | wx.BOTTOM | wx.LEFT, border=10)
        main_box.Add(btn5, pos=(25, 2), flag=wx.TOP | wx.BOTTOM, border=10)

        main_box.Add(self.table, pos=(5, 0), span=(20, 10), flag=wx.EXPAND | wx.ALL, border=10)

        btn1.Bind(wx.EVT_BUTTON, self.on_new)
        btn2.Bind(wx.EVT_BUTTON, self.on_search)
        btn3.Bind(wx.EVT_BUTTON, self.on_delete)
        btn4.Bind(wx.EVT_BUTTON, self.on_pre_search)
        btn5.Bind(wx.EVT_BUTTON, self.on_next_search)
        self.table.Bind(wx.EVT_KEY_DOWN, self.on_press_key)
        self.table.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.on_double_click)

        self.SetSizerAndFit(main_box)

    # 键盘按键事件
    def on_press_key(self, e):
        self.copy(e)

    # ctrl+c复制
    def copy(self, e):
        cell_value = self.table.GetCellValue(self.table.GetGridCursorRow(), self.table.GetGridCursorCol())
        if e.ControlDown() and e.GetKeyCode() == 67:
            clipboard = wx.TextDataObject()
            clipboard.SetText(cell_value)
            if wx.TheClipboard.Open():
                wx.TheClipboard.SetData(clipboard)
                wx.TheClipboard.Close()

    # 单元格双击显示明细
    def on_double_click(self, e):
        order_id = self.table.GetCellValue(e.GetRow(), 0)
        if order_id:
            ChildFrame(parent=self, title='查看', order_id=order_id)

    # 新建触发
    def on_new(self, e):
        ChildFrame(parent=self, title='新增')

    # 查询触发
    def on_search(self, e):
        # 先清空表格
        self.table.ClearGrid()
        orders_count = self.show_data(0)

        page_nums = math.ceil(orders_count / self.table.row)
        cur_page_num = 0 if page_nums == 0 else 1
        self.st20.SetLabelText('%s/%s' % (cur_page_num, page_nums))

    def on_delete(self, e):
        rows = self.table.get_selected_rows()
        if rows:
            order_ids = [self.table.GetCellValue(row, 0) for row in rows]
            if any(order_ids):
                if self.check_delete_dialog():
                    sql = 'delete from orders where order_id=?'
                    for order_id in order_ids:
                        DB_CONN.delete(sql, [order_id])
                    self.on_search(e)

    def check_delete_dialog(self):
        check_box = wx.MessageDialog(self, "确定要删除吗?", '警告', wx.YES_NO)
        code = check_box.ShowModal()
        if code == wx.ID_YES:
            return True
        else:
            return False

    def check_focus_cell(self):
        row = self.table.GetGridCursorRow()
        order_id = self.table.GetCellValue(row, 0)
        if not order_id:
            wx.MessageDialog(self, "未选中任何数据!", '', wx.OK).ShowModal()
            return None
        return row

    # 上一页触发
    def on_pre_search(self, e):
        page_info = self.st20.GetLabelText()
        cur_page_num, page_nums = [int(i) for i in page_info.split('/')]
        pre_page_num = cur_page_num - 1
        if pre_page_num > 0:
            # 先清空表格
            self.table.ClearGrid()
            self.show_data((pre_page_num-1)*self.table.row)
            self.st20.SetLabelText('%s/%s' % (pre_page_num, page_nums))

    # 下一页触发
    def on_next_search(self, e):
        page_info = self.st20.GetLabelText()
        cur_page_num, page_nums = [int(i) for i in page_info.split('/')]
        next_page_num = cur_page_num + 1
        if next_page_num <= page_nums:
            # 先清空表格
            self.table.ClearGrid()
            self.show_data((next_page_num-1) * self.table.row)
            self.st20.SetLabelText('%s/%s' % (next_page_num, page_nums))

    # 单元格显示数据
    def show_data(self, skip):
        conditions = '1=1 '
        conditions_value = []
        tc_keys = [
            'order_id',
            'order_time',
            'pay_time',
            'car_frame',
            'car_id',
            'car_type',
            'mile',
            'car_user',
            'phone',
            'total_pay',
            'insurance_name',
            'insurance_time',
            'remark'
        ]
        tc_values = [
            self.tc1.GetValue(),
            self.tc2.GetValue(),
            self.tc3.GetValue(),
            self.tc4.GetValue(),
            self.tc5.GetValue(),
            self.tc6.GetValue(),
            self.tc7.GetValue(),
            self.tc8.GetValue(),
            self.tc9.GetValue(),
            self.tc10.GetValue(),
            self.tc12.GetValue(),
            self.tc13.GetValue(),
            self.tc11.GetValue()
        ]

        for index, value in enumerate(tc_values):
            if value.strip():
                conditions += 'and %s like ? ' % tc_keys[index]
                conditions_value.append(value)

        # 取分页总数
        count_sql = 'select count(1) from orders where %s' % conditions
        select_sql = \
        '''
        select 
            order_id,
            car_id,
            car_type,
            car_user,
            phone,
            car_frame,
            order_time,
            pay_time,
            mile,
            total_pay,
            insurance_name,
            insurance_time,
            remark 
        from orders where %s order by order_id desc limit %s,%s
        ''' \
        % (conditions, skip, self.table.row)

        try:
            count_res = DB_CONN.query(count_sql, conditions_value)
            res = DB_CONN.query(select_sql, conditions_value)
        except:
            wx.MessageBox(traceback.format_exc(), '错误', wx.ICON_ERROR)
            return

        if count_res:
            count = count_res[0][0]
        else:
            count = 0

        for row, line in enumerate(res):
            for col, value in enumerate(line):
                self.table.set_cell_value(row, col, value)
        return count


class MainGrid(MyGrid):
    def __init__(self, parent):
        super(MainGrid, self).__init__(parent=parent)

        self.row = 25
        self.col = 13

        self._create()

    def _create(self):
        self.CreateGrid(self.row, self.col)

        self.SetColLabelValue(0, '结算单号')
        self.SetColLabelValue(1, '车牌号码')
        self.SetColLabelValue(2, '车辆类型')
        self.SetColLabelValue(3, '车主姓名')
        self.SetColLabelValue(4, '联系电话')
        self.SetColLabelValue(5, '车架号码')
        self.SetColLabelValue(6, '开单日期')
        self.SetColLabelValue(7, '结算日期')
        self.SetColLabelValue(8, '本次里程')
        self.SetColLabelValue(9, '合计金额')
        self.SetColLabelValue(10, '保险公司')
        self.SetColLabelValue(11, '保险到期')
        self.SetColLabelValue(12, '备注信息')

        self.SetDefaultColSize(110)
        self.SetDefaultRowSize(19)
        self.SetColSize(3, 60)
        self.SetColSize(8, 50)
        self.SetColSize(9, 50)
        self.SetColSize(12, 200)

        for row in range(self.row):
            for col in range(self.col):
                self.SetReadOnly(row, col)
                self.SetCellRenderer(row, col, wx.grid.GridCellAutoWrapStringRenderer())








