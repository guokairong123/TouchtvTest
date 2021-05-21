from airtest.core.android.android import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
adb = ADB()
devicesList = adb.devices()
print(devicesList)
poco = AndroidUiautomationPoco(device=[devicesList[0][0]], use_airtest_input=True, screenshot_each_action=False)


def setup_method():
    stop_app("com.touchtv.boluo")
    start_app("com.touchtv.boluo")
