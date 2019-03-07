import wx


class UI(wx.Frame):

    def __init__(self,):
        super(UI, self).__init__(None,style=wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE)

        self.window_size = (1000,600)
        self.cell_size = (60,42)

        self.__init()

    def __init(self):
        self.panel = wx.Panel(self)
        # 菜单栏
        menubar = wx.MenuBar()
        fix_order = wx.Menu()
        menubar.Append(fix_order, '&维修工单')
        self.SetMenuBar(menubar)

        # 工具栏
        self.toolbar = self.CreateToolBar()
        # print(self.toolbar.GetMargins())
        # self.toolbar.SetMargins(100,200)
        # print(self.toolbar.GetMargins())

        fix_order_new = self.toolbar.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('../icons/fix_order_new.png'),'新建')
        fix_order_save = self.toolbar.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('../icons/fix_order_save.png'), '保存')
        fix_order_delete = self.toolbar.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('../icons/fix_order_delete.png'), '删除')
        self.toolbar.AddSeparator()
        fix_order_delete2 = self.toolbar.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('../icons/fix_order_delete.png'))

        self.toolbar.Realize()
        self.Bind(wx.EVT_TOOL, self.ShowMessage, fix_order_new)
        self.Bind(wx.EVT_TOOL, self.close, fix_order_save)
        self.Bind(wx.EVT_TOOL, self.close, fix_order_delete)
        self.Bind(wx.EVT_TOOL, self.close, fix_order_delete2)

        # 布局
        main_box = wx.GridBagSizer()
        main_box.SetEmptyCellSize(self.cell_size)
        st_order_id = wx.StaticText(self.panel, label="结算单号: ",style=wx.ALIGN_LEFT)
        main_box.Add(st_order_id,pos=(0,0), flag=wx.TOP|wx.BOTTOM|wx.LEFT,border=10)
        tc_order_id = wx.TextCtrl(self.panel)
        main_box.Add(tc_order_id,pos=(0,1), span=(1,2), flag=wx.EXPAND|wx.TOP|wx.BOTTOM,border=10)

        st_order_time = wx.StaticText(self.panel, label="开单时间: ", style=wx.ALIGN_LEFT)
        main_box.Add(st_order_time, pos=(0,3), flag=wx.TOP|wx.BOTTOM|wx.LEFT,border=10)
        tc_order_time = wx.TextCtrl(self.panel)
        main_box.Add(tc_order_time, pos=(0,4), span=(1,4), flag=wx.EXPAND|wx.TOP|wx.BOTTOM,border=10)

        st_car_frame = wx.StaticText(self.panel, label="车架号: ", style=wx.ALIGN_LEFT)
        main_box.Add(st_car_frame, pos=(0, 8), flag=wx.TOP | wx.BOTTOM | wx.LEFT, border=10)
        tc_car_frame = wx.TextCtrl(self.panel)
        main_box.Add(tc_car_frame, pos=(0, 9), span=(1, 2), flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=10)

        st_car_id = wx.StaticText(self.panel, label="车牌号: ", style=wx.ALIGN_LEFT)
        main_box.Add(st_car_id, pos=(1,0), flag=wx.TOP|wx.BOTTOM|wx.LEFT,border=10)
        tc_car_id = wx.TextCtrl(self.panel)
        main_box.Add(tc_car_id, pos=(1,1), span=(1,2), flag=wx.EXPAND|wx.TOP|wx.BOTTOM,border=10)

        st_car_type = wx.StaticText(self.panel, label="车型: ", style=wx.ALIGN_LEFT)
        main_box.Add(st_car_type, pos=(1,3), flag=wx.TOP|wx.BOTTOM|wx.LEFT,border=10)
        tc_car_type = wx.TextCtrl(self.panel)
        main_box.Add(tc_car_type, pos=(1,4), span=(1,2), flag=wx.EXPAND|wx.TOP|wx.BOTTOM,border=10)

        st_car_owner = wx.StaticText(self.panel, label="车主: ", style=wx.ALIGN_LEFT)
        main_box.Add(st_car_owner, pos=(2, 0), flag=wx.TOP | wx.BOTTOM | wx.LEFT, border=10)
        tc_car_owner = wx.TextCtrl(self.panel)
        main_box.Add(tc_car_owner, pos=(2, 1), span=(1, 2), flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=10)

        st_phone = wx.StaticText(self.panel, label="联系电话: ", style=wx.ALIGN_LEFT, )
        main_box.Add(st_phone, pos=(2, 3), flag=wx.TOP | wx.BOTTOM | wx.LEFT, border=10)
        tc_phone = wx.TextCtrl(self.panel)
        main_box.Add(tc_phone, pos=(2, 4), span=(1, 2), flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=10)

        st_remark = wx.StaticText(self.panel, label="备注: ", style=wx.ALIGN_LEFT)
        main_box.Add(st_remark,pos=(1,6), flag=wx.ALL,border=10)
        tc_remark = wx.TextCtrl(self.panel,style=wx.TE_MULTILINE)
        main_box.Add(tc_remark,pos=(1,7), span=(2,4), flag=wx.EXPAND|wx.ALL,border=10)

        self.lc = wx.ListCtrl(self.panel, 0, style=wx.LC_REPORT | wx.EXPAND,size=(800,300))
        columns = [
            '维修单号',
            '车牌号',
            '开单时间',
            '车架号',
            '车型',
            '本次里程',
            '车主姓名',
            '车主电话',
            '备注'
        ]
        for index, column in enumerate(columns):
            self.lc.InsertColumn(index, column)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.select, self.lc)
        main_box.Add(self.lc,pos=(4,0), span=(8,8), flag=wx.EXPAND|wx.BOTTOM | wx.LEFT,border=10)

        self.lc2 = wx.ListCtrl(self.panel, 0, style=wx.LC_REPORT | wx.EXPAND, size=(400, 300))
        columns2 = [
            '维修单号',
            '维修项目',
            '零件费',
            '备注'
        ]
        for index, column in enumerate(columns2):
            self.lc2.InsertColumn(index, column)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.select2, self.lc2)
        main_box.Add(self.lc2, pos=(4, 8), span=(4,4), flag=wx.EXPAND |wx.BOTTOM | wx.LEFT, border=10)

        # # size
        # main_box.AddGrowableRow(6)
        self.panel.SetSizerAndFit(main_box)
        self.SetSize(self.window_size)


        # 标题
        self.SetTitle('GUIME')
        # 居中
        self.Centre()

    def select2(self,e):
        choice = self.lc2.GetFirstSelected()
        item = self.lc2.GetItem(itemIdx=choice, col=0)
        textItem = item.GetText()
        print(textItem)

    def select(self,e):
        choice = self.lc.GetFirstSelected()
        item = self.lc.GetItem(itemIdx=choice, col=0)
        textItem = item.GetText()
        print(textItem)

    def on_size(self,e):
        self.panel.size = self.GetSize()

    def set_values(self,data):
        if not isinstance(data,list):
            raise Exception('参数错误')
        for k,v in enumerate(data):
            index = self.lc.InsertItem(self.lc.GetItemCount(), k)
            for _k,_v in enumerate(v):
                self.lc.SetItem(index, _k, _v)
                # self.lc.SetColumnWidth(_k, wx.LIST_AUTOSIZE)
        self.lc.Focus(2)

    def show(self):
        self.Show()

    def close(self, e):
        self.Close()

    def ShowMessage(self,e):
        wx.MessageBox('Download completed', 'Info',
                      wx.OK | wx.ICON_INFORMATION)


def main():

    app = wx.App()
    ex = UI()
    ex.set_values([['1','2','33333333111111111111122132134123413412341341sssssss','4','5','6','7','8','9']]*10)
    ex.show()
    app.MainLoop()


if __name__ == '__main__':
    main()

