# -*- coding:utf-8 -*-
import sys
import firefox
import json
import wx
import Application
import importlib
importlib.reload(sys)
'''
2.7中对中文相关的这样使用
reload(sys)
sys.setdefaultencoding('utf-8')
'''
# 人员信息存储地址
filename = Application.filename
#filename = r'D:\namefile.txt'
class TestWindow():

    def __init__(self,parent,id):
        app = wx.App()
        self.win = wx.Frame(parent, id, r'加班申请-V0506', size=(710, 350))
        self.panel = wx.Panel(self.win,id,(10,10),size = (710,350))
        self.win.Show()
        label1 = wx.StaticText(self.panel, id, "请选择加班日期及相应加班人员", (10, 10))
        label2 = wx.StaticText(self.panel, id, "周六加班人员", (10, 30))
        label3 = wx.StaticText(self.panel, id, "周日加班人员", (170, 35))
        self.add = wx.Button(self.panel, id, r'添加新员工', pos=(450, 150), size=(80, 25))
        self.namelable = wx.StaticText(self.panel, id, '登录工号', pos=(350, 50), size=(80, 25))
        self.name = wx.TextCtrl(self.panel,id,pos = (430,45),size = (100,25))
        self.numberlable = wx.StaticText(self.panel, id, '登录密码', pos=(350, 100), size=(80, 25))
        self.number = wx.TextCtrl(self.panel, id, pos=(430, 95), size=(100, 25),style = wx.TE_PASSWORD)
        self.application = wx.Button(self.panel, id, '登录', pos=(350, 150), size=(80, 25))
        self.warning1 = wx.StaticText(self.panel, id, "注1：这个小程序只适用火狐41版本，其他版本不兼容！", (350, 180))
        self.warning2 = wx.StaticText(self.panel, id, "注2：只能添加当周加班信息！", (350, 200))
        self.warning3 = wx.StaticText(self.panel, id, "注3：周一只能添加周六的加班，周二开始才能添加周日的加班！", (350, 220))
        self.dirc = {}
        self.namelist = []
        self.readfile()
        #print (json.dumps(self.dirc, encoding="UTF-8", ensure_ascii=False))
        self.newemployname = ''
        self.newemploynumber = ''
        self.checkboxlist.Bind(wx.EVT_CHECKLISTBOX, self.printchoice)
        self.checkboxlist2.Bind(wx.EVT_CHECKLISTBOX, self.printchoice2)
        self.application.Bind(wx.EVT_BUTTON,self.Applications)
        self.applys1 = []
        self.applys2 = []
        self.add.Bind(wx.EVT_BUTTON, self.newemployee)
        app.MainLoop()


    def readfile(self):
        self.namelist = []
        file = open(filename)
        i = 1
        for name in file.readlines():
            if i ==1 :
                self.namelist.append(name)
                index = name
                i = 2
            else :
                i = 1
                self.dirc[index] = name
                continue
        file.close()
        self.checkboxlist = wx.CheckListBox(self.panel, -1, (10, 60), wx.DefaultSize, self.namelist)
        self.checkboxlist2 = wx.CheckListBox(self.panel, -1, (170, 60), wx.DefaultSize, self.namelist)

    def save(self,event):
        # 保存新员工信息
        file = open(filename, 'a')

        if len(self.newemployname.GetValue())<1 or len(self.newemploynumber.GetValue())<1:
            dlg = wx.MessageDialog(None, '工号或者密码不能为空，请重新输入！',
                                   '提示',
                                   wx.OK | wx.ICON_INFORMATION
                                   # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()
        else:
            file.write(self.newemployname.GetValue()+ '\n')
            file.write(self.newemploynumber.GetValue()+ '\n')
            file.close()
            dlg = wx.MessageDialog(None, '保存成功',
                               '提示',
                               wx.OK | wx.ICON_INFORMATION
                               # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                )
            dlg.ShowModal()
            dlg.Destroy()
            self.newemployname.Clear()
            self.newemploynumber.Clear()
            self.readfile()

    def newemployee(self,event):
        app = wx.App()
        win = wx.Frame(None,-1,r'新员工信息添加',size = (300,200))
        panel = wx.Panel(win, -1, (10, 10), size=(300, 200))
        namelable = wx.StaticText(panel,-1,'员工姓名',pos = (10,10),size = (80,80),name = 'namelable')
        self.newemployname = wx.TextCtrl(panel,-1,pos = (100,10),size = (100,25))
        numberlable = wx.StaticText(panel,-1,'员工工号',pos = (10,40),name = 'numberlable')
        self.newemploynumber = wx.TextCtrl(panel,-1,pos = (100,40),size = (100,25))
        submit = wx.Button(panel,-1,'保存',pos = (100,75),size = (40,30))
        submit.Bind(wx.EVT_BUTTON,self.save)
        win.Show()
        app.MainLoop()

    #存储选择的加班人员信息
    def printchoice(self,event):
        index = event.GetSelection()
        #print('index:' + str(index))
        label = self.checkboxlist.GetString(index)
        list = []
        list.append(label)
        # print json.dumps(list, encoding="UTF-8", ensure_ascii=False)
        #print('list:' + str(list))
        if self.checkboxlist.IsChecked(index):
            for name in list :
                for index in self.dirc.keys():
                    if name == index:
                        self.applys1.append(self.dirc[index])
        else:
            for name in list:
                for index in self.dirc.keys():
                    if name == index:
                        self.applys1.remove(self.dirc[index])
        #print('周六加班:' + str(self.applys1))

    def printchoice2(self,event):
        index = event.GetSelection()
        label = self.checkboxlist2.GetString(index)
        list = []
        list.append(label)
        #print json.dumps(self.applys2, encoding="UTF-8", ensure_ascii=False)
        if self.checkboxlist2.IsChecked(index):
            for name in list :
                for index in self.dirc.keys():
                    if name == index:
                        self.applys2.append(self.dirc[index])
        else:
            for name in list:
                for index in self.dirc.keys():
                    if name == index:
                        self.applys2.remove(self.dirc[index])

        #print ('周日加班：'+str(self.applys2))


    def Applications(self,event):
        if self.applys1 or self.applys2:
            if self.name.GetValue():
                if self.number.GetValue():
                    number = self.name.GetValue()
                    password = self.number.GetValue()
                    test = firefox.Firefox(self.applys1, self.applys2,number,password)
                else:
                    dlg = wx.MessageDialog(None, '请先输入登录密码！',
                                           '提示',
                                           wx.OK | wx.ICON_INFORMATION
                                           # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                           )
                    dlg.ShowModal()
                    dlg.Destroy()
            else:
                dlg = wx.MessageDialog(None, '请先输入登录用户名！',
                                       '提示',
                                       wx.OK | wx.ICON_INFORMATION
                                       # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                       )
                dlg.ShowModal()
                dlg.Destroy()
        else:
            dlg = wx.MessageDialog(None, '请选择加班人员！',
                                   '提示',
                                   wx.OK | wx.ICON_INFORMATION
                                   # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()




def main():
    win = TestWindow(parent=None,id= -1)
if __name__ == '__main__':main()
