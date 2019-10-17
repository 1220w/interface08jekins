import unittest

from case.TestIHRMEmploye import TestIHRMEmp
from case.TestIHRMUser import TestIHRMUser

suite = unittest.TestSuite()

suite.addTest(TestIHRMUser("test_login_success"))
suite.addTest(TestIHRMEmp("test_emp_add"))
suite.addTest(TestIHRMEmp("test_emp_uppdate"))
suite.addTest(TestIHRMEmp("test_emp_delete"))
#
runner = unittest.TextTestRunner()
runner.run(suite)
