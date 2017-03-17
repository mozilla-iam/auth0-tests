from selenium.webdriver.common.by import By

from pages.base import Base


class Auth0(Base):
    _login_with_ldap_button_locator = (By.CSS_SELECTOR, '.auth0-lock-ldap-button.auth0-lock-ldap-big-button')
    _ldap_email_field_locator = (By.CSS_SELECTOR, '.auth0-lock-input-email .auth0-lock-input')
    _ldap_password_field_locator = (By.CSS_SELECTOR, '.auth0-lock-input-password .auth0-lock-input')
    _login_button_locator = (By.CSS_SELECTOR, '.auth0-lock-submit')
    _login_with_email_button_locator = (By.CSS_SELECTOR, '.auth0-lock-passwordless-button')
    _passwordless_email_field_locator = (By.CSS_SELECTOR, '.auth0-lock-passwordless-pane .auth0-lock-input')
    _send_email_button_locator = (By.CSS_SELECTOR, '.auth0-lock-passwordless-submit')
    _login_with_github_button_locator = (By.CSS_SELECTOR, 'button.auth0-lock-social-button[data-provider="github"]')
    _github_username_field_locator = (By.ID, 'login_field')
    _github_password_field_locator = (By.ID, 'password')
    _github_sign_in_button_locator = (By.CSS_SELECTOR, '.btn.btn-primary.btn-block')
    _login_with_google_button_locator = (By.CSS_SELECTOR, 'button.auth0-lock-social-button[data-provider="google-oauth2"]')
    _google_email_field_locator = (By.ID, 'Email')
    _google_password_field_locator = (By.ID, 'Passwd')
    _next_button_locator = (By.ID, 'next')
    _google_sign_in_button_locator = (By.ID, 'signIn')

    def click_login_with_ldap(self):
        self.wait_for_element_visible(*self._login_with_ldap_button_locator)
        self.selenium.find_element(*self._login_with_ldap_button_locator).click()

    def enter_ldap_email(self, ldap_email):
        self.selenium.find_element(*self._ldap_email_field_locator).send_keys(ldap_email)

    def enter_ldap_password(self, ldap_password):
        self.selenium.find_element(*self._ldap_password_field_locator).send_keys(ldap_password)

    def click_login_button(self):
        self.selenium.find_element(*self._login_button_locator).click()

    def click_login_with_email(self):
        self.wait_for_element_visible(*self._login_with_email_button_locator)
        self.selenium.find_element(*self._login_with_email_button_locator).click()

    def enter_email(self, email):
        self.wait_for_element_visible(*self._passwordless_email_field_locator)
        self.selenium.find_element(*self._passwordless_email_field_locator).send_keys(email)

    def click_send_email(self):
        self.selenium.find_element(*self._send_email_button_locator).click()

    def click_login_with_github(self):
        self.wait_for_element_visible(*self._login_with_github_button_locator)
        self.selenium.find_element(*self._login_with_github_button_locator).click()

    def enter_github_username(self, username):
        self.selenium.find_element(*self._github_username_field_locator).send_keys(username)

    def enter_github_password(self, password):
        self.selenium.find_element(*self._github_password_field_locator).send_keys(password)

    def click_github_sign_in(self):
        self.wait_for_element_visible(*self._github_sign_in_button_locator)
        self.selenium.find_element(*self._github_sign_in_button_locator).click()

    def click_login_with_google(self):
        self.wait_for_element_visible(*self._login_with_google_button_locator)
        self.selenium.find_element(*self._login_with_google_button_locator).click()

    def enter_google_email(self, email):
        self.wait_for_element_visible(*self._google_email_field_locator)
        self.selenium.find_element(*self._google_email_field_locator).send_keys(email)

    def click_next(self):
        self.selenium.find_element(*self._next_button_locator).click()

    def enter_google_password(self, password):
        self.wait_for_element_visible(*self._google_password_field_locator)
        self.selenium.find_element(*self._google_password_field_locator).send_keys(password)

    def click_google_sign_in(self):
        self.selenium.find_element(*self._google_sign_in_button_locator).click()
