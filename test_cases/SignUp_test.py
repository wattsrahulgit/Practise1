from PageObjectModels import Objects
from utilities.ElementLocators import ElementLocators
from selenium.webdriver.common.keys import Keys


class TestSignUpPage(ElementLocators):

    def test_SignUpPage(self):

        signUp = Objects.SignUpElements(self.driver)

        signUp.clickRegister().click()
        signUp.selectMale().click()
        signUp.enterFirstName().send_keys("Test1")
        signUp.enterLastName().send_keys("Test2")
        signUp.enterEmail().send_keys("abcefddf@xyz.com")
        signUp.enterPassword().send_keys("qwerty@123")
        signUp.enterConfirmPWD().send_keys("qwerty@123")
        signUp.finalRegister().click()

        alertText = signUp.getSuccessMessage().text
        assert ("Your registration completed" in alertText)

        signUp.clickContinue().click()
