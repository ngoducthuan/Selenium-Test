import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin:
    base_url = "http://127.0.0.1:5000/"

    @classmethod
    def setup_class(cls):
        # Thiết lập trình duyệt một lần cho cả class
        cls.driver = webdriver.Chrome()
        cls.driver.set_window_size(812, 886)

    @classmethod
    def teardown_class(cls):
        # Đóng trình duyệt sau khi tất cả các bài kiểm tra hoàn thành
        cls.driver.quit()

    def login(self, username, password):
        """
        Hàm tiện ích để thực hiện đăng nhập.
        """
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID, "username").clear()
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

    @pytest.mark.parametrize("username, password, expected_text", [
        ("admin", "1", "Dashboard"),  # Đăng nhập đúng
        ("admin", "1234", "Invalid username or password"),  # Sai mật khẩu
        ("nonexistent", "1", "Invalid username or password"),  # Tài khoản không tồn tại
        ("", "1", "Username is required"),  # Tên đăng nhập trống
        ("admin", "", "Password is required"),  # Mật khẩu trống
        ("admin", "a" * 300, "Invalid username or password"),  # Mật khẩu quá dài
        ("admin", " ", "Password is required"),  # Mật khẩu là khoảng trắng
        ("<script>alert(1)</script>", "1", "Invalid username or password"),  # Tên đăng nhập chứa ký tự đặc biệt
    ])
    def test_login_cases(self, username, password, expected_text):
        """
        Kiểm tra các trường hợp đăng nhập.
        """
        self.login(username, password)
        assert expected_text in self.driver.page_source, f"Failed for username={username}, password={password}"


if __name__ == "__main__":
    # Chạy các bài kiểm tra
    pytest.main(["-v", __file__])
