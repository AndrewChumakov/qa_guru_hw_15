import pytest
from selene import browser


@pytest.fixture(scope="function",
                params=[(1920, 1080), (1440, 900), (3840, 2160)],
                ids=["desktop_1920x1080", "desktop_1440x900", "desktop_3840x2160"])
def desktop_browser(request):
    browser.config.base_url = "https://github.com"
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(scope="function",
                params=[(414, 896), (360, 640), (384, 854)],
                ids=["mobile_418x896", "mobile_360x640", "mobile_384x854"])
def mobile_browser(request):
    browser.config.base_url = "https://github.com"
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(scope="function",
                params=[(1920, 1080), (1440, 900), (360, 640), (384, 854)],
                ids=["desktop_1920x1080", "desktop_1440x900", "mobile_360x640", "mobile_384x854"])
def desktop_or_mobile_browser(request):
    browser.config.base_url = "https://github.com"
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width <= 1024:
        yield "mobile"
    else:
        yield "desktop"
    browser.quit()
