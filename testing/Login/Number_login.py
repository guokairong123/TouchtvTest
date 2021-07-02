
class Test_Number_Login:

    def test_click_my(self, d):
        d.poco_click(text="我的")
        # 首次打开我的会存在这个元素
        if(d.poco_exists(name="com.touchtv.touchtv:id/tv_push_tip")):
            d.poco_click(name="com.touchtv.touchtv:id/tv_push_tip")
            d.poco_click(name="com.touchtv.touchtv:id/br_login_btn")
        else:
            d.poco_click(name="com.touchtv.touchtv:id/br_login_btn")

