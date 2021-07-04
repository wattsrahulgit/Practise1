from selenium.webdriver.common.by import By


class signUpElements:

    def __init__(self, driver):
        self.driver = driver

    Register = (By.CSS_SELECTOR, ".ico-register")
    Male = (By.ID, "gender-male")
    Female = (By.ID, "gender-female")
    FirstName = (By.ID, "FirstName")
    LastName = (By.ID, "LastName")
    Email = (By.ID, "Email")
    Password = (By.CSS_SELECTOR, "#Password")
    ConfirmPassword = (By.CSS_SELECTOR, "#ConfirmPassword")
    RegisterButton = (By.CSS_SELECTOR, "#register-button")
    SuccessMessage = (By.CSS_SELECTOR, ".result")
    Continue = (By.CSS_SELECTOR, "[class='button-1 register-continue-button']")
