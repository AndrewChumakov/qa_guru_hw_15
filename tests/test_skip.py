"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser

from pages.main_page import MainPage

github_page = MainPage()


def test_github_desktop(desktop_or_mobile_browser):
    if desktop_or_mobile_browser == "mobile":
        pytest.skip("Это тест для десктопного разрешения")
    browser.open("/")
    github_page.sign_in_desktop()


def test_github_mobile(desktop_or_mobile_browser):
    if desktop_or_mobile_browser == "desktop":
        pytest.skip("Это тест для мобильного разрешения")
    browser.open("/")
    github_page.sign_in_mobile()
