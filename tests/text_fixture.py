"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

from selene import browser

from pages.main_page import MainPage

github_page = MainPage()


def test_github_desktop(desktop_browser):
    browser.open("/")
    github_page.sign_in_desktop()


def test_github_mobile(mobile_browser):
    browser.open("/")
    github_page.sign_in_mobile()
