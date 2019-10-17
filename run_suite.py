import unittest

from case.TestIHRMEmploye import TestIHRMEmp
from case.TestIHRMUser import TestIHRMUser
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()

suite.addTest(TestIHRMUser("test_login_success"))
suite.addTest(TestIHRMEmp("test_emp_add"))
suite.addTest(TestIHRMEmp("test_emp_uppdate"))
suite.addTest(TestIHRMEmp("test_emp_delete"))
#
file_to = "./report/report.html"
with open(file_to, "wb")as f:
    runner = HTMLTestRunner(f, title ="我的测试报告",description="v1.0")
    # runner = unittest.TextTestRunner()

    runner.run(suite)

