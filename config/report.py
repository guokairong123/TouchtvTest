import os
import time
from distutils.sysconfig import get_python_lib

import allure
from airtest.core.android.adb import ADB
from airtest.core.api import auto_setup
from airtest.report.report import simple_report
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

pkdir = get_python_lib().lower()
rootpath = os.path.dirname(os.path.dirname(__file__)).replace('\\','/')
log_path = os.path.abspath(os.path.dirname(os.getcwd())) + '/log'


class Report:
    def __init__(self):
        # adb = ADB()
        # devicesList = adb.devices()
        # # print(devicesList)
        # self.poco = AndroidUiautomationPoco(devices=[devicesList[0][0]], use_airtest_input=True,
        #                                screenshot_each_action=False)
        pass


def air_report(func):
    def _wrap(*args, **kwargs):
        print("调用到了")
        print("这是 " + __file__)
        curdir_time = str(int(time.time()))
        logdir = log_path + '/' + curdir_time + '/' + func.__name__
        print("日志路径：" + logdir)
        os.makedirs(logdir)
        auto_setup(__file__, logdir=logdir, project_root=True)
        print(func)
        func(*args)
        logfile = logdir + f'/{func.__name__}.html'
        simple_report(__file__, logpath=logdir, output=logfile)
        time.sleep(2)
        print("这是啥: " + pkdir)
        with open(logfile, 'r+', encoding='utf-8') as f:
            context = f.read()
            temp = context.replace(os.path.dirname(rootpath), '')
            print("看看：", os.path.dirname(rootpath))
        # print(temp)
        allure.attach(temp, 'report.html', attachment_type=allure.attachment_type.HTML)
        # print(func.__name__)
    return _wrap
