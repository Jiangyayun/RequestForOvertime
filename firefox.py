#-*- coding:utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import window
import weekend
class Firefox:
    def __init__(self,namelist1,namelist2,number,password):
        #profile_directory = r'C:\yn80ouvt.default'
        #profile = webdriver.FirefoxProfile(profile_directory)
        #profile.accept_untrusted_certs = True
        #self.browser = webdriver.Firefox(profile)
        self.browser = webdriver.Firefox()
        #self.browser = webdriver.Ie()
        self.browser.implicitly_wait(10)

        #加载正式oa环境
        self.browser.get(u'aaa')

        self.number = number
        self.password = password

        self.namelist1 = namelist1
        self.namelist2 = namelist2
        self.lenth1 = len(self.namelist1)
        self.lenth2 = len(self.namelist2)
        self.lenth3 = self.lenth1+self.lenth2
        self.namelist = namelist1+namelist2



        #print '周六加班：'+str(self.namelist1)
        #print '周日加班：'+str(self.namelist2)
        self.login()

    def login(self):
        '''
        #输入用户名
        elemu = self.browser.find_element_by_name("username")
        elemu.send_keys(self.number)
        #输入密码
        elemp = self.browser.find_element_by_name("password")
        elemp.send_keys(self.password)
        #点击登录
        elems = self.browser.find_element_by_xpath('/html/body/div/div[2]/form/table/tbody/tr[4]/td/a/span')
        #print 'browser.current_window_handle is :',self.browser.current_window_handle
        elems.click()
        '''


        elemu = self.browser.find_element_by_name("username")
        elemu.send_keys(self.number)
        elemp = self.browser.find_element_by_name("password")
        elemp.send_keys(self.password)
        elems = self.browser.find_element_by_xpath('//*[@id="submit_btn"]')
        #print 'browser.current_window_handle is :', self.browser.current_window_handle
        elems.click()

        locator = (By.LINK_TEXT,'个人工作台')
        #time.sleep(3)
        try:
            #找到个人工作台然后到个人工作台界面点击节点进入加班申请界面
            WebDriverWait(self.browser,20,0.5).until(EC.presence_of_all_elements_located(locator))
            #测试环境的个人平台
            # elemgrpt1 = self.browser.find_element_by_xpath('/html/body/div[5]/div/ul/li[2]/a/span')
            #//*[@id="soa_nav"]/div/ul/li[3]/a/span
            elemgrpt1= self.browser.find_element_by_xpath('//*[@id="soa_nav"]/div/ul/li[3]/a/span')
            elemgrpt1.click()
            #测试环境的个人平台
            #elemgrpt2 = self.browser.find_element_by_xpath('/html/body/div[4]/div/ul/li[2]/a/span')
            elemgrpt2 = self.browser.find_element_by_xpath('//*[@id="soa_nav"]/div/ul/li[3]/a/span')
            elemgrpt2.click()
        finally:
            #把页面的滚动条拉倒最底下，这样才能找到人事等等那些元素，否则就会找不到然后报错
            js = "document.documentElement.scrollTop = 10000"
            self.browser.execute_script(js)
            # 先进入第一层iframe
            self.browser.switch_to.frame(self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/iframe'))
            #time.sleep(3)
            # 再进入第二次frame
            self.browser.switch_to.frame(self.browser.find_element_by_xpath('/html/body/iframe[2]'))
            #time.sleep(5)
            #elemgrbg = self.browser.find_element_by_id('treeDemo_23_span')
            #测试环境的个人办公
            # elemgrbg = self.browser.find_element_by_xpath('//*[@id="treeDemo_22_span"]')
            elemgrbg = self.browser.find_element_by_xpath('//*[@id="treeDemo_13_span"]')
            elemgrbg.click()
            # 再第二层frame里面找到需要定位的元素,需要一层一层的打开定位到最小的一个节点上

        # 打开人事类节点
        #time.sleep(10)
        #elemrsl = self.browser.find_element_by_id('treeDemo_32_span')
        #测试环境的人事类
        # elemrsl = self.browser.find_element_by_xpath('//*[@id="treeDemo_31_span"]')
        #elemrsl = self.browser.find_element_by_xpath('//*[@id="treeDemo_24_span"]')
        elemrsl = self.browser.find_element_by_xpath('//*[@id="treeDemo_25_span"]')
        #//*[@id="treeDemo_25_span"]
        elemrsl.click()
        # 打开加调班节点
        #elemjtb = self.browser.find_element_by_id('treeDemo_38_a')
        #测试环境的加调班
        # elemjtb = self.browser.find_element_by_xpath('//*[@id="treeDemo_37_span"]')
        #elemjtb = self.browser.find_element_by_xpath('//*[@id="treeDemo_29_span"]')
        elemjtb = self.browser.find_element_by_xpath('//*[@id="treeDemo_30_span"]')
        elemjtb.click()
        # 点击云商加调班新界面
        #elemjb = self.browser.find_element_by_id('treeDemo_51_span')
        #测试环境数据
        # elemjb = self.browser.find_element_by_xpath('//*[@id="treeDemo_50_span"]')
        #elemjb = self.browser.find_element_by_xpath('//*[@id="treeDemo_40_span"]')
        elemjb = self.browser.find_element_by_xpath('//*[@id="treeDemo_41_span"]')
        elemjb.click()
        # 退出iframe，返回列表操作
        self.browser.switch_to.default_content()
        # 查看有几个窗口
        handles = self.browser.window_handles

        '''
        locator = (By.LINK_TEXT,'外部顾问加班申请')
        #time.sleep(3)
        try:
            WebDriverWait(self.browser,20,0.5).until(EC.presence_of_all_elements_located(locator))
            self.browser.switch_to.frame(self.browser.find_element_by_xpath('//*[@id="homeFrame"]'))
            #time.sleep(13)
            elemgrpt = self.browser.find_element_by_xpath('/html/body/div/dl[2]/dd[5]/div/a')
            #print '已经找到加班申请，准备点击了'
            elemgrpt.click()
            #print '已经点击完成'
            #time.sleep(6)
        finally:
            # 查看有几个窗口
            handles = self.browser.window_handles
            #print '已经找到iframe'
        '''

        '''
        for handle in handles:
            if handle!= self.browser.current_window_handle:
                print 'swtich to',handle
            else:
                print 'handle is :',handle
        '''


        #切换到新的窗口
        self.browser.switch_to.window(self.browser.window_handles[1])
        #print 'browser.current_window_handle :',self.browser.current_window_handle

        time.sleep(5)
        #获取当前界面的alert
        alert1 = self.browser.switch_to.alert
        alert1.accept()

        #调加班申请
        self.add(self.namelist)

        #点击提交按钮
        elemsubmit = self.browser.find_element_by_xpath('/html/body/form/div/div[1]/a[3]/p')
        elemsubmit.click()

        #弹窗确认
        self.browser.switch_to.frame(self.browser.find_element_by_id('layui-layer-iframe1'))
        #点击确认按钮
        submit32 = self.browser.find_element_by_id('Submit32')
        submit32.click()

        '''
        #测试阶段，把确认去掉，改成点击取消了
        time.sleep(3)
        elemcancel = self.browser.find_element_by_xpath('/html/body/div/div[3]/input[2]')
        elemcancel.click()
        '''

        self.browser.switch_to.default_content()
        #提交后，点击关闭
        elemclose = self.browser.find_element_by_xpath('/html/body/div/div[2]/a')
        elemclose.click()

        '''
        #点击退出的,然后退出加班申请界面
        time.sleep(5)
        elemquit = self.browser.find_element_by_xpath('/html/body/form/div/div[1]/a[1]')
        elemquit.click()
        '''


        self.browser.switch_to.window(self.browser.window_handles[0])
        #elemlogout = self.browser.find_element_by_xpath('//*[@id="logout"]')
        #elemlogout.click()
        self.browser.quit()

    def add(self,namelist):
        index1 = 0
        index2 = 1
        lenth = len(namelist)
        #/html/body/form/div/div[3]/div/table/tbody/tr/td/table/tbody/tr[3]/td[2]/span/input[5]
        #/html/body/form/div/div[3]/div/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/span/input[5]
        for num in namelist:
            #输入工号，自动带出姓名
            numberid = 'ProcessHrAddShift_empNo_'+str(index1)
            elemnumber = self.browser.find_element_by_id(numberid)
            elemnumber.send_keys(num)
            #点击姓名框，带出姓名
            name1 = 'ProcessHrAddShift_empName_'
            nameid = name1 + str(index1)
            elemname = self.browser.find_element_by_id(nameid)
            elemname.click()

            #选择加班日期
            dateid = 'ProcessHrAddShift_addDate_'+str(index1)
            elemdate = self.browser.find_element_by_id(dateid)
            elemdate.click()
            elemdatechoose = self.browser.find_element_by_id(dateid)
            saturday = weekend.saturday
            sunday = weekend.sunday
            if index2>self.lenth1:
                date = sunday
            else:date = saturday
            elemdatechoose.send_keys(date)
            #elemdate.send_keys(date)

            #选择原班次
            ybcid = 'NameAndCode_'+str(index1)
            elemybc = self.browser.find_element_by_id(ybcid)
            elemybc.click()


            #选择申请加班班次
            bc1 = '/html/body/form/div/div[3]/div/table/tbody/tr'
            bc3 = '/td/table/tbody/tr[3]/td[2]/span/input[5]'
            if lenth == 0:
                bcid = bc1 + bc3
            else:
                bc2 = '[' + str(index2) + ']'
                bcid = bc1 + bc2 +bc3
            elembc = self.browser.find_element_by_xpath(bcid)
            #/html/body/form/div/div[3]/div/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/span/input[5]

            elembc.click()

            #弹出班次的选择窗口window
            handles = self.browser.window_handles
            self.browser.switch_to.window(self.browser.window_handles[2])
            #print 'browser.current_window is :',self.browser.current_window_handle

            #选择第一个2001班次
            elembcchoose = self.browser.find_element_by_xpath('//*[@id="chk"]')
            elembcchoose.click()

            #点击确定
            elembcsure = self.browser.find_element_by_xpath('/html/body/form/div/div/div/a[1]')
            elembcsure.click()


            #回到原来的窗口
            handles = self.browser.window_handles
            self.browser.switch_to.window(self.browser.window_handles[1])


            #选择加班原因
            jbyy1 = '/html/body/form/div/div[3]/div/table/tbody/tr'
            jbyy3 = '/td/table/tbody/tr[3]/td[3]/span/select/option[8]'
            if lenth == 0 :
                jbyyid = jbyy1 + jbyy3
            else:
                jbyy2 = '[' + str(index2) + ']'
                jbyyid = jbyy1 + jbyy2 + jbyy3
            elemreason = self.browser.find_element_by_xpath(jbyyid)
            elemreason.click()

            #填写加班原因
            gzap1 = 'ProcessHrAddShift_adShiftReasonDetail_'
            gzapid = gzap1 +str(index1)
            elemdetail = self.browser.find_element_by_id(gzapid)
            elemdetail.send_keys(u'版本时间紧张，需加班完成')
            #newbrowser = browse
            #browser.switch_to.window(browser.window_handles[0])

            #点击增加，新加加班人员信息
            if lenth>1:
                elemadd = self.browser.find_element_by_xpath('/html/body/form/div/div[3]/div/div/a[1]')
                elemadd.click()
                lenth = lenth-1
                index1 +=1
                index2 +=1



def main():
    list1 = []
    list2 = []
    number = ''
    password = ''
    win = Firefox(list1,list2,number,password)

if __name__ == '__main__':main()
