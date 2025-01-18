from Browser_Package.openbrowser import start_browser
from Browser_Package.closebroser import close_browser

class TestCases:
    def test_case(self):
        start_browser()
        print("hello running TC")
        close_browser()

obj_tc = TestCases()
obj_tc.test_case()


