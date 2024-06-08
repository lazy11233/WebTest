import logging
import pytest
from selenium import webdriver
import subprocess
import os
import allure
from datetime import datetime

logger = logging.getLogger(__name__)
log_dir = "logs"


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # 确保你已经安装了 ChromeDriver 并在 PATH 中
    yield driver
    driver.quit()


def pytest_sessionfinish(session, exitstatus):
    """Hook for generating Allure report after tests are done."""
    if not os.path.exists("reports/allure-results"):
        print("Allure results directory not found!")
        return

    print("Allure generate reports/allure-results -o reports/allure-reports --clean")
    report_dir = "reports/allure-reports"
    subprocess.run(["allure", "generate", "reports/allure-results", "-o", report_dir, "--clean"])


def pytest_runtest_logreport(report):
    """Log each test result."""
    print(f"Test {report.nodeid} - {report.when}: {report.outcome}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # If the test failed, take a screenshot
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # Construct the screenshot file path
            screenshot_dir = os.path.join("screenshots", os.path.dirname(item.nodeid.replace("::", "_")))
            screenshot_path = os.path.join(screenshot_dir, f"{os.path.basename(item.nodeid.replace('::', '_'))}.png")

            # Ensure the directory exists
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)

            # Save the screenshot
            driver.save_screenshot(screenshot_path)

            # Attach the screenshot to the Allure report
            allure.attach.file(screenshot_path, name="screenshot", attachment_type=allure.attachment_type.PNG)


def pytest_configure(config):
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, datetime.now().strftime("log_%Y%m%d_%H%M%S.log"))
    config.option.log_file = log_file


def pytest_runtest_setup(item):
    print(f'开始执行测试用例{item.name}')


def pytest_runtest_teardown(item):
    print(f'结束执行测试用例{item.name}')
