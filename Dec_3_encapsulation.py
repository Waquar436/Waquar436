class BaseTest:
    def open_browser(self):
        print("starting the browser.")

    def close_browser(self):
        print("close browser")


class TestCase1(BaseTest):
    def test_positive(self):
        self.open_browser()
        print("Test case p1 executed.")
        self.close_browser()

    def test_negative(self):
        self.open_browser()
        print("Test case n1 executed.")
        self.close_browser()

class TestCase2(BaseTest):
    def test_positive(self):
        self.open_browser()
        print("Test case p1 executed.")
        self.close_browser()

    def test_negative(self):
        self.open_browser()
        print("Test case n1 executed.")
        self.close_browser()
