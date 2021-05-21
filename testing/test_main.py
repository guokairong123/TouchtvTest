from airtest.core.api import *

from config.common import AirtestPoco
from config.report import *


class TestMain:
    def setup_class(self):
        self.d = AirtestPoco()
        print("启动app")
        stop_app("com.touchtv.boluo")
        start_app("com.touchtv.boluo")
        time.sleep(2)

    @allure.story('登录流程')
    @allure.link('www.baidu.com')
    @allure.title('用例1')
    @air_report
    def test_start_app(self):
        self.d.poco_click(text="测试服务器")


if __name__ == "__main__":
    os.system('pytest -s -q test_main.py --alluredir ./../log/temp')
    os.system('allure generate ./../log/temp -o ./../log/report --clean')