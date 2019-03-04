import wx


class UI(wx.Frame):

    def __init__(self,):
        super(UI, self).__init__(None,style=wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE)

        self.window_size = (1200,600)

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
        main_box = wx.BoxSizer(wx.VERTICAL)

        top_box = wx.BoxSizer(wx.VERTICAL)

        line1 = wx.BoxSizer(wx.HORIZONTAL)
        st_order_id = wx.StaticText(self.panel, label="结算单号: ",style=wx.ALIGN_LEFT,size=(70,20))
        line1.Add(st_order_id,0, wx.ALIGN_LEFT | wx.TOP | wx.LEFT,15)
        tc_order_id = wx.TextCtrl(self.panel,size=(150,20))
        line1.Add(tc_order_id,0, wx.ALIGN_LEFT|wx.TOP,15)

        st_order_time = wx.StaticText(self.panel, label="开单时间: ", style=wx.ALIGN_LEFT,size=(70,20))
        line1.Add(st_order_time, 0, wx.ALIGN_LEFT | wx.TOP | wx.LEFT,15)
        tc_order_time = wx.TextCtrl(self.panel, size=(150,20))
        line1.Add(tc_order_time, 0, wx.ALIGN_LEFT | wx.TOP,15)

        st_out_time = wx.StaticText(self.panel, label="出厂时间: ", style=wx.ALIGN_LEFT,size=(70,20))
        line1.Add(st_out_time, 0, wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 15)
        tc_out_time = wx.TextCtrl(self.panel, size=(150, 20))
        line1.Add(tc_out_time, 0, wx.ALIGN_LEFT | wx.TOP, 15)

        st_pay_time = wx.StaticText(self.panel, label="结算时间: ", style=wx.ALIGN_LEFT,size=(70,20))
        line1.Add(st_pay_time, 0, wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 15)
        tc_pay_time = wx.TextCtrl(self.panel, size=(150, 20))
        line1.Add(tc_pay_time, 0, wx.ALIGN_LEFT | wx.TOP, 15)

        line2 = wx.BoxSizer(wx.HORIZONTAL)
        st_car_id = wx.StaticText(self.panel, label="车牌号: ", style=wx.ALIGN_LEFT,size=(70,20))
        line2.Add(st_car_id, 0, wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 15)
        tc_car_id = wx.TextCtrl(self.panel, size=(150, 20))
        line2.Add(tc_car_id, 0, wx.ALIGN_LEFT | wx.TOP, 15)

        st_car_type = wx.StaticText(self.panel, label="车型: ", style=wx.ALIGN_LEFT, size=(70, 20))
        line2.Add(st_car_type, 0, wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 15)
        tc_car_type = wx.TextCtrl(self.panel, size=(150, 20))
        line2.Add(tc_car_type, 0, wx.ALIGN_LEFT | wx.TOP, 15)

        st_car_owner = wx.StaticText(self.panel, label="车主: ", style=wx.ALIGN_LEFT, size=(70, 20))
        line2.Add(st_car_owner, 0, wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 15)
        tc_car_owner = wx.TextCtrl(self.panel, size=(150, 20))
        line2.Add(tc_car_owner, 0, wx.ALIGN_LEFT | wx.TOP, 15)

        st_phone = wx.StaticText(self.panel, label="联系电话: ", style=wx.ALIGN_LEFT, size=(70, 20))
        line2.Add(st_phone, 0, wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 15)
        tc_phone = wx.TextCtrl(self.panel, size=(150, 20))
        line2.Add(tc_phone, 0, wx.ALIGN_LEFT | wx.TOP, 15)

        line3 = wx.BoxSizer(wx.HORIZONTAL)
        st_car_frame = wx.StaticText(self.panel, label="车架号: ", style=wx.ALIGN_LEFT, size=(70, 20))
        line3.Add(st_car_frame, 0, wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 15)
        tc_car_frame = wx.TextCtrl(self.panel, size=(150, 20))
        line3.Add(tc_car_frame, 0, wx.ALIGN_LEFT | wx.TOP, 15)

        st_remark = wx.StaticText(self.panel, label="备注: ", style=wx.TE_MULTILINE, size=(70, 20))
        line3.Add(st_remark, 0, wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 15)
        tc_remark = wx.TextCtrl(self.panel, size=(400, 50))
        line3.Add(tc_remark, 0, wx.ALIGN_LEFT | wx.TOP, 15)

        top_box.Add(line1)
        top_box.Add(line2)
        top_box.Add(line3)

        bottom_box = wx.BoxSizer(wx.HORIZONTAL)
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
        bottom_box.Add(self.lc,0,wx.EXPAND | wx.TOP | wx.LEFT, 15)

        main_box.Add(top_box)
        main_box.Add(bottom_box)
        self.panel.SetSizer(main_box)
        # size
        # self.panel.SetSizerAndFit(main_box)
        # self.panel.Bind(wx.EVT_SIZE,self.on_size,self.panel)
        self.SetSize(self.window_size)
        # 标题
        self.SetTitle('GUIME')
        # 居中
        self.Centre()

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