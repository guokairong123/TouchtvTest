import pytest
from airtest.core.api import connect_device

from config.common import AirtestPoco


@pytest.fixture(scope='session')
def d():
    # device = connect_device("android:///")
    # driver = AirtestPoco(device)
    # print("运行conftest文件")
    driver = AirtestPoco()
    yield driver
