import traceback
import math
from datetime import datetime

import wx
import wx.grid
import wx.adv

from db import DB_CONN


orders_key = ['order_id', 'car_id', 'car_type', 'car_user', 'phone', 'car_frame', 'order_time', 'mile','remark']
orders_name = ['结算单号', '车牌号码', '车辆类型', '车主姓名', '联系电话', '车架号码', '开单时间', '本次里程','备注信息']
orders_map = dict(zip(orders_key, orders_name))

detail_key = ['order_id', 'project','price' ,'number','pay', 'remark']
detail_name = ['结算单号', '维修项目', '零件单价','零件数量','零件费用', '备注信息']
detail_map = dict(zip(detail_key, detail_name))


class MyFrame(wx.Frame):
    def __init__(self,title,size):
        super(MyFrame,self).__init__(parent=None,title=title,size=size)

        self.st_size = (100,25)

        self.tcs = {}

        self.panel = wx.Panel(self)
        self.main_box = wx.GridBagSizer()
        self._init_ui()
        self.panel.SetSizerAndFit(self.main_box)

        self.Centre()
        self.Show()

    def create_st(self,label,pos,span=(1,1),style=wx.ALIGN_RIGHT,size=None):
        if not size:
            size = self.st_size
        st = wx.StaticText(self.panel, label=label, style=style, size=size)
        self.main_box.Add(st, pos=pos, span=span, flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        return st

    def create_tc(self,name,pos,span=(1,1),style=0,size=None):
        if not size:
            size = self.st_size
        tc = wx.TextCtrl(self.panel,style=style,size=size)
        self.main_box.Add(tc, pos=pos, span=span, flag=wx.TOP | wx.BOTTOM, border=10)
        self.tcs[name] = tc
        return tc

    def create_button(self,name,pos,flag=wx.TOP,bind=None):
        btn = wx.Button(self.panel, -1, name)
        self.main_box.Add(btn, pos=pos, flag=flag, border=10)
        btn.Bind(wx.EVT_BUTTON, bind)

    def create_table(self):
        raise NotImplementedError

    def _init_ui(self):
        raise NotImplementedError

    def has_tc_value(self,tc):
        if tc.GetValue().strip():
            return True
        else:
            return False

    def get_tc_value(self,tc):
        return tc.GetValue().strip()

    def set_tc_value(self,tc,value):
        if isinstance(value,int):
            value = str(value)
        tc.SetValue(value)

    def get_cell_value(self,row,col):
        if hasattr(self,'table'):
            return self.table.GetCellValue(row,col)
        return None

    def set_cell_value(self,row,col,value):
        if hasattr(self,'table'):
            if isinstance(value,int):
                value = str(value)
            return self.table.SetCellValue(row,col,value)
        return None


class MainUI(MyFrame):
    def __init__(self,title='维修记录单管理软件',size=(1200, 750)):
        self.table_row_nums = 20
        self.table_col_nums = 9

        self.orders_key = orders_key
        self.orders_name = orders_name
        self.orders_map = orders_map

        super(MainUI, self).__init__(title,size)

    def create_table(self):
        self.table = wx.grid.Grid(self.panel, -1)
        self.table.CreateGrid(self.table_row_nums, self.table_col_nums)
        for row in range(self.table_row_nums):
            for col in range(self.table_col_nums):
                self.table.SetReadOnly(row,col)
        self.table.SetDefaultColSize(110)
        self.table.SetDefaultRowSize(22)
        self.table.SetColLabelValue(0, '结算单号')
        self.table.SetColLabelValue(1, '车牌号码')
        self.table.SetColLabelValue(2, '车辆类型')
        self.table.SetColLabelValue(3, '车主姓名')
        self.table.SetColSize(3, 70)
        self.table.SetColLabelValue(4, '联系电话')
        self.table.SetColLabelValue(5, '车架号码')
        self.table.SetColLabelValue(6, '开单时间')
        self.table.SetColLabelValue(7, '本次里程')
        self.table.SetColLabelValue(8, '备注信息')
        self.table.SetColSize(8, 200)
        self.table.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK,self.show_detail)
        self.table.Bind(wx.EVT_KEY_DOWN,self.on_key)
        self.main_box.Add(self.table, pos=(5, 0), span=(20, 8), flag=wx.EXPAND | wx.ALL, border=10)

    def _init_ui(self):
        self.create_st('结算单号', (1, 0))
        self.create_tc('order_id', (1, 1),style=wx.TE_PROCESS_ENTER)
        self.create_st('开单时间', (1, 2))
        self.create_tc('order_time', (1, 3), style=wx.TE_PROCESS_ENTER)
        self.create_st('车架号码', (1, 4))
        self.create_tc('car_frame', (1, 5), size=(220, 25),style=wx.TE_PROCESS_ENTER)
        self.create_st('车牌号码', (2, 0))
        self.create_tc('car_id', (2, 1),style=wx.TE_PROCESS_ENTER)
        self.create_st('车辆类型', (2, 2))
        self.create_tc('car_type', (2, 3),style=wx.TE_PROCESS_ENTER)
        self.create_st('车主姓名', (3, 0))
        self.create_tc('car_user', (3, 1),style=wx.TE_PROCESS_ENTER)
        self.create_st('联系电话', (3, 2))
        self.create_tc('phone', (3, 3),style=wx.TE_PROCESS_ENTER)
        self.create_st('备注信息', (2, 4))
        self.create_tc('remark', (2, 5), span=(2, 1), style=wx.TE_PROCESS_ENTER|wx.TE_MULTILINE, size=(220, 70))

        # 按回车搜索
        for tc in self.tcs.values():
            tc.Bind(wx.EVT_TEXT_ENTER,self.on_search)

        self.create_button('新建', (0, 0), wx.TOP | wx.LEFT, self.on_new)
        self.create_button('查询', (0, 1), bind=self.on_search)
        self.create_button('上一页', (25, 0),wx.TOP | wx.BOTTOM | wx.LEFT, bind=self.on_pre_search)
        self.page_info = self.create_st('0/0', (25, 1),style=wx.ALIGN_CENTER)
        self.create_button('下一页', (25, 2),wx.TOP | wx.BOTTOM, bind=self.on_next_search)

        self.create_table()

    def on_key(self,e):
        # ctrl c 复制
        self.copy(e)

    def copy(self,e):
        cell_value = self.get_cell_value(self.table.GetGridCursorRow(), self.table.GetGridCursorCol())
        if e.ControlDown() and e.GetKeyCode() == 67:
            clipboard = wx.TextDataObject()
            clipboard.SetText(cell_value)
            if wx.TheClipboard.Open():
                wx.TheClipboard.SetData(clipboard)
                wx.TheClipboard.Close()

    # 查询触发
    def on_search(self, e):
        # 先清空表格
        self.table.ClearGrid()
        orders_count = self.show_data(0)

        page_nums = math.ceil(orders_count / self.table_row_nums)
        cur_page_num = 0 if page_nums == 0 else 1
        self.page_info.SetLabelText('%s/%s'%(cur_page_num,page_nums))

    # 上一页触发
    def on_pre_search(self,e):
        page_info = self.page_info.GetLabelText()
        cur_page_num,page_nums = [int(i) for i in page_info.split('/')]
        pre_page_num = cur_page_num-1
        if pre_page_num>0:
            # 先清空表格
            self.table.ClearGrid()
            self.show_data((pre_page_num-1)*self.table_row_nums)
            self.page_info.SetLabelText('%s/%s' % (pre_page_num, page_nums))

    # 下一页触发
    def on_next_search(self,e):
        page_info = self.page_info.GetLabelText()
        cur_page_num,page_nums = [int(i) for i in page_info.split('/')]
        next_page_num = cur_page_num+1
        if next_page_num<=page_nums:
            # 先清空表格
            self.table.ClearGrid()
            self.show_data((next_page_num-1)*self.table_row_nums)
            self.page_info.SetLabelText('%s/%s' % (next_page_num, page_nums))

    # 单元格显示数据
    def show_data(self,skip):
        orders_key = self.orders_key.copy()
        orders_key.remove('mile')
        conditions = '1=1 '
        conditions_value = []
        for order_key in orders_key:
            ins = self.tcs[order_key]
            if self.has_tc_value(ins):
                conditions += 'and %s=? ' % order_key
                conditions_value.append(self.get_tc_value(ins))
        # 取分页总数
        count_sql = 'select count(1) from orders where %s'%conditions
        select_sql = \
        '''
        select order_id,car_id,car_type,car_user,phone,car_frame,order_time,mile,remark 
        from orders where %s order by order_id desc limit %s,%s
        ''' % (conditions, skip,self.table_row_nums)
        try:
            count = DB_CONN.query(count_sql,conditions_value)
            res = DB_CONN.query(select_sql, conditions_value)
        except:
            wx.MessageBox(traceback.format_exc(), '错误', wx.ICON_ERROR)
            return

        count = count[0][0]

        for row, line in enumerate(res):
            for col, value in enumerate(line):
                self.set_cell_value(row, col, value)
        return count

    # 新建触发
    def on_new(self,e):
        ChildFrame('新增')

    def show_detail(self, e):
        order_id = self.get_cell_value(self.table.GetGridCursorRow(),0)
        if order_id:
            ChildFrame('查看',order_id=order_id)


class ChildFrame(MyFrame):
    def __init__(self,title,size=(600,620),order_id=None):
        self.title = title
        self.table_row_nums = 10
        self.table_col_nums = 5
        self.order_id = order_id

        self.orders_key = orders_key
        self.orders_name = orders_name
        self.orders_map = orders_map

        self.detail_key = detail_key
        self.detail_name = detail_name
        self.detail_map = detail_map

        self.before_init()
        super(ChildFrame, self).__init__(self.title,size)
        self.after_init()

    def before_init(self):
        if self.title == '查看':
            select_order = \
            '''
            select order_id,car_id,car_type,car_user,phone,car_frame,order_time,mile,remark from orders where order_id=?
            '''
            self.order_info = DB_CONN.query(select_order, [self.order_id])
            if not self.order_info or not self.order_info[0]:
                self.order_info = None

            select_detail = 'select project,price,number,pay,remark from detail where order_id=?'
            self.detail_info = DB_CONN.query(select_detail, [self.order_id])
            if not self.detail_info:
                self.detail_info = None

    def after_init(self):
        if self.title == '查看':
            if self.order_info:
                order_info = self.order_info[0]
                self.set_tc_value(self.tcs['order_id'],order_info[0])
                self.set_tc_value(self.tcs['car_id'],order_info[1])
                self.set_tc_value(self.tcs['car_type'],order_info[2])
                self.set_tc_value(self.tcs['car_user'],order_info[3])
                self.set_tc_value(self.tcs['phone'],order_info[4])
                self.set_tc_value(self.tcs['car_frame'],order_info[5])
                self.set_tc_value(self.tcs['order_time'],order_info[6])
                self.set_tc_value(self.tcs['mile'], order_info[7])
                self.set_tc_value(self.tcs['remark'],order_info[8])

            if self.detail_info:
                for row,value in enumerate(self.detail_info):
                    if row>=10:
                        self.table.AppendRows()
                    for col in range(self.table_col_nums):
                        self.set_cell_value(row, col, value[col])
        else:
            gen_id = generate_id(DB_CONN)
            today = datetime.strftime(datetime.now(), '%Y-%m-%d')
            self.set_tc_value(self.tcs['order_id'], gen_id)
            self.set_tc_value(self.tcs['order_time'], today)

    def create_table(self):
        self.table = wx.grid.Grid(self, -1)
        self.table.CreateGrid(self.table_row_nums, self.table_col_nums)
        self.table.SetDefaultRowSize(25)
        self.table.SetColLabelValue(0, '维修项目')
        self.table.SetColSize(0, 100)
        self.table.SetColLabelValue(1, '零件单价')
        self.table.SetColSize(1, 50)
        self.table.SetColLabelValue(2, '零件数量')
        self.table.SetColSize(2, 50)
        self.table.SetColLabelValue(3, '零件费用')
        self.table.SetColSize(3, 50)
        self.table.SetColLabelValue(4, '备注信息')
        self.table.SetColSize(4, 200)
        self.main_box.Add(self.table, pos=(7, 0), span=(10, 4), flag=wx.EXPAND | wx.ALL, border=10)

    def _init_ui(self):
        self.create_st('结算单号', (1, 0))
        self.create_tc('order_id', (1, 1), style=wx.TE_READONLY)
        self.create_st('车架号码', (1, 2))
        self.create_tc('car_frame', (1, 3), size=(220, 25))
        self.create_st('车牌号码', (2, 0))
        self.create_tc('car_id', (2, 1))
        self.create_st('开单时间', (2, 2))
        self.create_tc('order_time', (2, 3), size=(220, 25))
        self.create_st('车辆类型', (3, 0))
        self.create_tc('car_type', (3, 1))
        self.create_st('本次里程', (3, 2))
        self.create_tc('mile', (3, 3))
        self.create_st('车主姓名', (4, 0))
        self.create_tc('car_user', (4, 1))
        self.create_st('备注信息', (4, 2))
        self.create_tc('remark', (4, 3), span=(2, 1), size=(220, 70))
        self.create_st('联系电话', (5, 0))
        self.create_tc('phone', (5, 1))

        self.create_button('添加', (6, 0), wx.TOP | wx.LEFT, self.on_add_rows)
        self.create_button('删除', (6, 1), bind=self.on_delete_rows)
        self.create_button('保存', (6, 2), bind=self.on_save_rows)

        self.create_table()

    # 添加触发
    def on_add_rows(self,e):
        self.table.AppendRows()

    # 删除触发
    def on_delete_rows(self,e):
        if self.table.SelectedRows:
            up = 0
            for x in self.table.SelectedRows:
                self.table.DeleteRows(x-up)
                if self.table.GetNumberRows() < self.table_row_nums:
                    self.table.AppendRows()
                up += 1
        else:
            row = self.table.GetGridCursorRow()
            self.table.DeleteRows(row)
            if self.table.GetNumberRows() < self.table_row_nums:
                self.table.AppendRows()

    # 保存触发
    def on_save_rows(self,e):
        # 保存正在编辑的单元格中的数据
        self.table.SaveEditControlValue()
        try:
            self.save_main_order()
            self.save_detail()
        except Exception as e:
            wx.MessageBox(str(e), '错误', wx.ICON_ERROR)
            return
        wx.MessageBox('保存成功!', '完成', wx.OK)

    # 保存主单据
    def save_main_order(self):
        tcs = self.orders_key
        value = []
        for i in tcs:
            ins = self.tcs[i]
            value.append(self.get_tc_value(ins))

        # upsert
        insert_sql = \
        '''
        replace into orders(order_id,car_id,car_type,car_user,phone,car_frame,order_time,mile,remark)
        values (?,?,?,?,?,?,?,?,?)
        '''
        DB_CONN.insert(insert_sql,[value])

    # 保存明细
    def save_detail(self):
        order_id = self.get_tc_value(self.tcs['order_id'])
        rows = self.table.GetNumberRows()
        values = []
        for row in range(rows):
            line = [order_id]
            for col in range(self.table_col_nums):
                cell_value = self.get_cell_value(row, col)
                line.append(cell_value)

            if any(line[1:]):
                values.append(line)
        delete_sql = 'delete from detail where order_id=?'
        DB_CONN.delete(delete_sql,[(order_id,)])
        if values:
            insert_sql = 'insert into detail(order_id,project,price,number,pay,remark) values (?,?,?,?,?,?)'
            DB_CONN.insert(insert_sql,values)


# 自动生成单号
def generate_id(conn):
    today = datetime.strftime(datetime.now(), '%Y%m%d')
    begin = '001'
    sql = 'select max(order_id) from orders'
    try:
        res = conn.query(sql)[0][0]
        if res is None or not res.startswith(today):
            return today + begin
        else:
            inx = int(res[-3:]) + 1
            return '%s%03d' % (today, inx)
    except:
        raise Exception('单号生成错误!')


def run():
    app = wx.App()
    MainUI()
    app.MainLoop()


if __name__ == '__main__':
    run()
