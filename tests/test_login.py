import pytest
from selenium import webdriver
from login_page import LoginPage


class TestLoginPage:
    @pytest.fixture(scope="class")
    def setup(self, request):
        driver = webdriver.Chrome()
        request.cls.driver = driver
        yield
        driver.quit()

    @pytest.fixture(autouse=True)
    def setup_login_page(self, setup):
        self.login_page = LoginPage(self.driver)
        self.login_page.load("http://127.0.0.1:8080/")

    def test_login_successful(self):
        self.login_page.login("user1", "password1")
        assert self.login_page.get_message() == "Login successful"

    def test_login_failed_wrong_password(self):
        self.login_page.login("user1", "wrongpassword")
        assert self.login_page.get_message() == "Login failed"

    def test_login_failed_nonexistent_user(self):
        self.login_page.login("nonexistentuser", "password")
        assert self.login_page.get_message() == "Login failed"


if __name__ == "__main__":
    pytest.main()
