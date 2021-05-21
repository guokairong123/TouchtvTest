
import allure
from airtest.core import api
from airtest.core.api import connect_device
from airtest.core.cv import Template
from airtest.core.helper import log
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


class AirtestPoco:
    def __init__(self):
        self.api = api
        device = connect_device("android:///")
        self.poco = AndroidUiautomationPoco(device, use_airtest_input=True,
                                            screenshot_each_action=False)
        self.timeout = 20

    @allure.step("元素点击：")
    def touch(self, v: Template, **kwargs):
        """
        在设备屏幕上执行触摸操作
        :param v: 要触摸的目标，可以是Template实例，也可以是绝对坐标（x，y）
        :param kwargs: [times  要执行多少次触摸]
        """
        self.api.touch(v, **kwargs)

    def poco_obj(self, **kwargs):
        """poco实例"""
        if 'index' in kwargs:
            index = kwargs.pop('index')
            ele = self.poco(**kwargs)[index]
        else:
            ele = self.poco(**kwargs)
        ele.wait_for_appearance(timeout=self.timeout)
        return ele

    @allure.step("poco点击元素：")
    def poco_click(self, **kwargs):
        """
        对由UI代理表示的UI元素执行click操作。如果这个UI代理代表一组
        UI元素，单击集合中的第一个元素，并将UI元素的定位点用作默认值
        一个。还可以通过提供“focus”参数单击另一个点偏移。
        :param kwargs: [text, name]
        """
        log("点击元素：{}".format(kwargs))
        self.poco_obj(**kwargs).click()
        self.poco.sleep_for_polling_interval()
