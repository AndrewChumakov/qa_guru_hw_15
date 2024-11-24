"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser

from pages.main_page import MainPage

desktop = pytest.mark.parametrize("desktop_browser", [(1920, 1080), (3840, 2160)],
                                  indirect=True,
                                  ids=["desktop_1920x1080", "desktop_3840x2160"])
mobile = pytest.mark.parametrize("mobile_browser", [(360, 640), (384, 854)],
                                 indirect=True,
                                 ids=["mobile_418x896", "mobile_384x854"])

github_page = MainPage()


@desktop
def test_github_desktop(desktop_browser):
    browser.open("/")
    github_page.sign_in_desktop()


@mobile
def test_github_mobile(mobile_browser):
    browser.open("/")
    github_page.sign_in_mobile()