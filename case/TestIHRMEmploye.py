import requests
import unittest

# 创建测试类
import app
from api.EmpAPI import EmpADUG


class TestIHRMEmp(unittest.TestCase):
    # 初始化函数
    def setUp(self):
        self.session = requests.Session()
        self.emp_obj = EmpADUG()

    # 销毁资源函数
    def tearDown(self):
        self.session.close()

    #  创建测试类
    def test_emp_add(self):
        response = self.emp_obj.emp_add(self.session, "程笑3", "17865655595", "45989461")
        print("新增成功响应的结果：", response.json().get("data").get("id"))
        id = response.json().get("data").get("id")
        app.ID = id

    def test_emp_uppdate(self):
        response = self.emp_obj.emp_update(self.session,app.ID,
                                           username="程小1")
        print("修改后的响应体:", response.json())

        self.assertEqual(True, response.json().get("success"))

    def test_emp_get(self):
        response = self.emp_obj.emp_get(self.session, app.ID)
        print("查询到的用户信息:", response.json())
        self.assertEqual(10000, response.json().get("code"))

    def test_emp_delete(self):
        response = self.emp_obj.emp_delete(self.session, app.ID)
        print("删除的响应结果:", response.json())
        self.assertIn("操作成功", response.json().get("message"))
