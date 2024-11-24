from selene import browser, be

class MainPage:
    def sign_in_desktop(self):
        browser.element(".HeaderMenu-link--sign-up").click()
        browser.element("#email").should(be.visible)

    def sign_in_mobile(self):
        browser.element(".Button--link").click()
        self.sign_in_desktop()