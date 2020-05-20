from datetime import datetime

import wx
import wx.grid

from db import DB_CONN
from utils import generate_id

from .textctrl import MyTextCtrl
from .grid import MyGrid
from .panel import MyPanel


class ChildFrame(wx.Frame):
    def __init__(self, parent, title, size=(620, 720), order_id=None):
        super(ChildFrame, self).__init__(parent=parent, title=title, size=size)

        ChildPanel(self, order_id)

        self.Centre()
        self.Show()


class ChildPanel(MyPanel):
    def __init__(self, parent, order_id=None):
        super(ChildPanel, self).__init__(parent=parent)

        self._create()
        self._after_create(order_id)

    def _create(self):
        main_box = wx.GridBagSizer()

        st1 = wx.StaticText(self, label='结算单号', style=wx.ALIGN_RIGHT, size=(100, 25))
        st2 = wx.StaticText(self, label='车架号码', style=wx.ALIGN_RIGHT, size=(100, 25))
        st3 = wx.StaticText(self, label='车牌号码', style=wx.ALIGN_RIGHT, size=(100, 25))
        st4 = wx.StaticText(self, label='开单日期', style=wx.ALIGN_RIGHT, size=(100, 25))
        st5 = wx.StaticText(self, label='车辆类型', style=wx.ALIGN_RIGHT, size=(100, 25))
        st6 = wx.StaticText(self, label='结算日期', style=wx.ALIGN_RIGHT, size=(100, 25))
        st7 = wx.StaticText(self, label='车主姓名', style=wx.ALIGN_RIGHT, size=(100, 25))
        st8 = wx.StaticText(self, label='本次里程', style=wx.ALIGN_RIGHT, size=(100, 25))
        st9 = wx.StaticText(self, label='联系电话', style=wx.ALIGN_RIGHT, size=(100, 25))
        st10 = wx.StaticText(self, label='合计', style=wx.ALIGN_RIGHT, size=(100, 25))
        st11 = wx.StaticText(self, label='备注信息', style=wx.ALIGN_RIGHT, size=(100, 25))
        st12 = wx.StaticText(self, label='保险公司', style=wx.ALIGN_RIGHT, size=(100, 25))
        st13 = wx.StaticText(self, label='保险到期', style=wx.ALIGN_RIGHT, size=(100, 25))

        self.tc1 = MyTextCtrl(self, style=wx.TE_READONLY, size=(100, 25))
        self.tc2 = MyTextCtrl(self, size=(200, 25))
        self.tc3 = MyTextCtrl(self, style=wx.TE_PROCESS_ENTER, size=(100, 25))
        self.tc4 = MyTextCtrl(self, size=(100, 25))
        self.tc5 = MyTextCtrl(self, size=(100, 25))
        self.tc6 = MyTextCtrl(self, size=(100, 25))
        self.tc7 = MyTextCtrl(self, size=(100, 25))
        self.tc8 = MyTextCtrl(self, size=(100, 25))
        self.tc9 = MyTextCtrl(self, size=(100, 25))
        self.tc10 = MyTextCtrl(self, size=(100, 25))
        self.tc11 = MyTextCtrl(self, size=(200, 70))
        self.tc12 = MyTextCtrl(self, size=(100, 25))
        self.tc13 = MyTextCtrl(self, size=(100, 25))

        btn1 = wx.Button(self, label='添加')
        btn2 = wx.Button(self, label='删除')
        btn3 = wx.Button(self, label='保存')

        self.table = ChildGrid(self)

        main_box.Add(st1, pos=(1, 0), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st2, pos=(1, 2), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st3, pos=(2, 0), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st4, pos=(2, 2), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st5, pos=(3, 0), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st6, pos=(3, 2), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st7, pos=(4, 0), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st8, pos=(4, 2), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st9, pos=(5, 0), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st10, pos=(5, 2), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st11, pos=(7, 0), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st12, pos=(6, 0), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        main_box.Add(st13, pos=(6, 2), flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)

        main_box.Add(self.tc1, pos=(1, 1), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc2, pos=(1, 3), span=(1, 2), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc3, pos=(2, 1), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc4, pos=(2, 3), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc5, pos=(3, 1), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc6, pos=(3, 3), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc7, pos=(4, 1), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc8, pos=(4, 3), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc9, pos=(5, 1), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc10, pos=(5, 3), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc11, pos=(7, 1), span=(2, 2), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc12, pos=(6, 1), flag=wx.TOP | wx.BOTTOM, border=10)
        main_box.Add(self.tc13, pos=(6, 3), flag=wx.TOP | wx.BOTTOM, border=10)

        main_box.Add(btn1, pos=(9, 0), flag=wx.TOP | wx.LEFT, border=10)
        main_box.Add(btn2, pos=(9, 1), flag=wx.TOP, border=10)
        main_box.Add(btn3, pos=(9, 2), flag=wx.TOP, border=10)

        main_box.Add(self.table, pos=(10, 0), span=(10, 4), flag=wx.EXPAND | wx.ALL, border=10)

        self.tc10.set_value('0')
        self.tc3.Bind(wx.EVT_TEXT_ENTER, self.on_auto_fillin)
        btn1.Bind(wx.EVT_BUTTON, self.on_add)
        btn2.Bind(wx.EVT_BUTTON, self.on_delete)
        btn3.Bind(wx.EVT_BUTTON, self.on_save)

        self.SetSizerAndFit(main_box)

    def _after_create(self, order_id):
        if order_id:
            select_order = \
            '''
            select 
                order_id,
                car_frame,
                car_id,
                order_time,
                car_type,
                pay_time,
                mile,
                car_user,
                phone,
                total_pay,
                insurance_name,
                insurance_time,
                remark
            from orders where order_id=?
            '''

            select_detail = \
            '''
            select 
                project,
                price,
                number,
                pay,
                remark 
            from detail where order_id=?
            '''

            order_info = DB_CONN.query(select_order, [order_id])
            if order_info and order_info[0]:
                info = order_info[0]
                self.tc1.set_value(info[0])
                self.tc2.set_value(info[1])
                self.tc3.set_value(info[2])
                self.tc4.set_value(info[3])
                self.tc5.set_value(info[4])
                self.tc6.set_value(info[5])
                self.tc7.set_value(info[6])
                self.tc8.set_value(info[7])
                self.tc9.set_value(info[8])
                self.tc10.set_value(info[9])
                self.tc12.set_value(info[10])
                self.tc13.set_value(info[11])
                self.tc11.set_value(info[12])

            detail_info = DB_CONN.query(select_detail, [order_id])
            if detail_info:
                for row, value in enumerate(detail_info):
                    if row >= 10:
                        self.table.AppendRows()
                        self.table.row += 1
                    for col in range(self.table.col):
                        self.table.set_cell_value(row, col, value[col])

        else:
            gen_id = generate_id(DB_CONN)
            today = datetime.strftime(datetime.now(), '%Y.%m.%d')
            self.tc1.set_value(gen_id)
            self.tc4.set_value(today)

    def on_auto_fillin(self, e):
        car_id = self.tc3.GetValue()
        if car_id:
            sql = 'select car_type,car_user,phone from orders where car_id=? limit 1'
            res = DB_CONN.query(sql, [car_id])
            if res and res[0]:
                car_type = res[0][0]
                car_user = res[0][1]
                phone = res[0][2]
                self.tc5.set_value(car_type)
                self.tc7.set_value(car_user)
                self.tc8.set_value(phone)

    def on_add(self, e):
        self.table.AppendRows()
        self.table.row += 1

    def on_delete(self, e):
        rows = self.table.get_selected_rows()
        if rows:
            for row in sorted(rows, reverse=True):
                self.table.DeleteRows(row)
                if self.table.GetNumberRows() < self.table.row:
                    self.table.AppendRows()

    def on_save(self, e):
        # 保存正在编辑的单元格中的数据
        self.table.SaveEditControlValue()
        try:
            self.set_total_pay()
            self.save_order()
            self.save_detail()
        except Exception as e:
            wx.MessageBox(str(e), '错误', wx.ICON_ERROR)
            return
        wx.MessageBox('保存成功!', '完成', wx.OK)

    def set_total_pay(self):
        total_pay = 0
        rows = self.table.GetNumberRows()
        for row in range(rows):
            pay = self.table.GetCellValue(row, 3) or '0'
            if not pay.isdigit():
                raise Exception('请输入正确的费用!')
            total_pay += int(pay)
        self.tc10.set_value(str(total_pay))
        # return total_pay

    # 保存主单据
    def save_order(self):
        values = [
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
            self.tc11.GetValue(),
        ]
        replace_sql = \
        '''
        replace into orders
        (
            order_id,
            car_frame,
            car_id,
            order_time,
            car_type,
            pay_time,
            car_user,
            mile,
            phone,
            total_pay,
            insurance_name,
            insurance_time,
            remark
        )
        values (?,?,?,?,?,?,?,?,?,?,?,?,?)
        '''
        DB_CONN.insert(replace_sql, [values])

    # 保存明细
    def save_detail(self):
        order_id = self.tc1.GetValue()
        values = []
        for row in range(self.table.row):
            line = [order_id]
            for col in range(self.table.col):
                cell_value = self.table.GetCellValue(row, col)
                line.append(cell_value)

            if any(line[1:]):
                values.append(line)
        delete_sql = 'delete from detail where order_id=?'
        DB_CONN.delete(delete_sql, [order_id])
        if values:
            insert_sql = 'insert into detail(order_id,project,price,number,pay,remark) values (?,?,?,?,?,?)'
            DB_CONN.insert(insert_sql, values)


class ChildGrid(MyGrid):
    def __init__(self, parent, row=10, col=5):
        super(ChildGrid, self).__init__(parent=parent)

        self.row = row
        self.col = col

        self._create()

    def _create(self):
        self.CreateGrid(self.row, self.col)

        self.SetColLabelValue(0, '维修项目')
        self.SetColLabelValue(1, '单价')
        self.SetColLabelValue(2, '数量')
        self.SetColLabelValue(3, '费用')
        self.SetColLabelValue(4, '备注信息')

        self.SetDefaultRowSize(20)
        self.SetColSize(0, 250)
        self.SetColSize(1, 50)
        self.SetColSize(2, 50)
        self.SetColSize(3, 50)
        self.SetColSize(4, 100)

        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.on_auto_set_pay)

        for row in range(self.row):
            for col in range(self.col):
                self.SetCellRenderer(row, col, wx.grid.GridCellAutoWrapStringRenderer())

    # 自动设置pay=price*nums
    def on_auto_set_pay(self, e):
        col = e.GetCol()
        if col == 3:
            row = e.GetRow()
            price = self.GetCellValue(row, 1)
            nums = self.GetCellValue(row, 2)
            if price.strip().isdigit() and nums.strip().isdigit():
                total_pay = int(price) * int(nums)
                self.set_cell_value(row, 3, str(total_pay))
        e.Skip()