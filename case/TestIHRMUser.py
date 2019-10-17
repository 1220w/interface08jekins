# 导包
import json
import unittest
from parameterized import parameterized

import app
from api.UserAPI import UserLogin
import requests


def read_json():
    data = []
    with open(app.PRO_PATH + "/data/login_data.json", "r", encoding="utf-8")as f:
        for value in json.load(f).values():
            mobile = value.get('mobile')
            password = value.get("password")
            success = value.get("success")
            code = value.get("code")
            message = value.get("message")
            # ele = (mobile, password, success, code, message)
            data.append((mobile, password, success, code, message))
    return data


# 创建测试类

class TestIHRMUser(unittest.TestCase):
    # 初始化函数
    def setUp(self):
        self.session = requests.Session()
        # 实例化api对象
        self.api = UserLogin()

    # 关闭函数
    def tearDown(self):
        self.session.close()

    # 测试函数登录
    @parameterized.expand(read_json())
    def test_login(self, mobile, password, success, code, message):
        # 登录请求业务
        response = self.api.login(self.session, mobile, password)
        # 请求断言业务

        print(response.json())

        self.assertEqual(success, response.json().get("success"))
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(message, response.json().get("message"))

    # 测试函数：只实现登录成功
    def test_login_success(self):
        print("登陆成功接口")
        # 请求业务
        response1 = self.api.login(self.session, "13800000002", "123456")
        # 断言业务
        result = response1.json()
        print("登陆成功的响应结果", result)
        self.assertEqual(True, result.get("success"))
        self.assertEqual(10000, result.get("code"))
        self.assertIn("操作成功", result.get("message"))
        token = result.get("data")
        print("登陆成功后的token值", token)
        app.TOKEN = token
