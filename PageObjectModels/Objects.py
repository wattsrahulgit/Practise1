import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjectModels.SignUp import signUpElements


class ApplicationElements:

    def __init__(self, driver):
        self.driver = driver

    Computers = (By.LINK_TEXT, "Computers")
    Desktops = (By.LINK_TEXT, "Desktops")
    OrderBy = (By.CSS_SELECTOR, "#products-orderby")
    SortBy = (By.CSS_SELECTOR, "[id='products-orderby'] option")
    Customer_Service = (By.CSS_SELECTOR, "[class='column customer-service']")
    Expensive_Desktop = (By.LINK_TEXT, "Build your own expensive computer")
    FreeShip = (By.CSS_SELECTOR, "[class='free-shipping']")
    SearchItem = (By.CSS_SELECTOR, "#small-searchterms")
    RadioButtons = (By.CSS_SELECTOR, "input[type='radio']")
    Software = (By.CSS_SELECTOR, "input[type='checkbox']")
    Quantity = (By.CSS_SELECTOR, "#addtocart_74_EnteredQuantity")
    AddToCart = (By.XPATH, "//input[@class='button-1 add-to-cart-button']")
    Cart= (By.CSS_SELECTOR, ".cart-qty")
    ApplyGiftCard = (By.CSS_SELECTOR, ".gift-card-coupon-code")
    Country = (By.ID, "CountryId")
    Province = (By.ID, "StateProvinceId")
    EstimateShip = (By.CSS_SELECTOR, "[value='Estimate shipping']")
    CommonButtons = (By.CSS_SELECTOR, ".common-buttons")
    Agreement = (By.CSS_SELECTOR, "#termsofservice")
    CheckOut = (By.CSS_SELECTOR, "#checkout")
    Guest = (By.CSS_SELECTOR, "[value='Checkout as Guest']")
    Error = (By.XPATH, "//span[contains(text(),'First name is required.')]")
    ContinueButton = (By.XPATH, "//div[@id='billing-buttons-container']/input")

    def getComputers(self):
        return self.driver.find_element(*ApplicationElements.Computers)

    def getDesktops(self):
        return self.driver.find_element(*ApplicationElements.Desktops)

    def getOrderBy(self):
        return self.driver.find_element(*ApplicationElements.OrderBy)

    def getSortBy(self):
        return self.driver.find_elements(*ApplicationElements.SortBy)

    def getCustomerService(self):
        return self.driver.find_element(*ApplicationElements.Customer_Service)

    def getExpensiveDesktop(self):
        return self.driver.find_element(*ApplicationElements.Expensive_Desktop)

    def MoveElement(self, Element):
        action = ActionChains(self.driver)
        return action.move_to_element(Element).perform()

    def checkFreeShip(self):
        return self.driver.find_element(*ApplicationElements.FreeShip)

    def checkSearchItems(self):
        return self.driver.find_element(*ApplicationElements.SearchItem)

    def selectConfig(self):
        return self.driver.find_elements(*ApplicationElements.RadioButtons)

    def selectSoftware(self):
        return self.driver.find_elements(*ApplicationElements.Software)

    def EnterQuantity(self):
        return self.driver.find_element(*ApplicationElements.Quantity)

    def CartValue(self):
        return self.driver.find_element(*ApplicationElements.AddToCart)

    def ScrollUp(self):
        return self.driver.execute_script("window.scrollTo(0, 0)")

    def FinalCart(self):
        return self.driver.find_element(*ApplicationElements.Cart)

    def AddGift(self):
        return self.driver.find_element(*ApplicationElements.ApplyGiftCard)

    def selectCountry(self):
        state = Select(self.driver.find_element(*ApplicationElements.Country))
        return state

    def selectProvince(self):
        Province = Select(self.driver.find_element(*ApplicationElements.Province))
        return Province

    def ShippingEstimation(self):
        self.driver.find_element(*ApplicationElements.EstimateShip)

    def getCommonButtons(self):
        return self.driver.find_element(*ApplicationElements.CommonButtons)

    def selectAgreement(self):
        return self.driver.find_element(*ApplicationElements.Agreement)

    def FinalCheckout(self):
        return self.driver.find_element(*ApplicationElements.CheckOut)

    def ContinueGuest(self):
        return self.driver.find_element(*ApplicationElements.Guest)

    def ErrorMessageCheck(self):
        return self.driver.find_element(*ApplicationElements.Error)

    def clickContinue(self):
        return self.driver.find_element(*ApplicationElements.ContinueButton)


class SignUpElements:

    def __init__(self, driver):
        self.driver = driver

    def clickRegister(self):
        return self.driver.find_element(*signUpElements.Register)

    def selectMale(self):
        return self.driver.find_element(*signUpElements.Male)

    def selectFemale(self):
        return self.driver.find_element(*signUpElements.Female)

    def enterFirstName(self):
        return self.driver.find_element(*signUpElements.FirstName)

    def enterLastName(self):
        return self.driver.find_element(*signUpElements.LastName)

    def enterEmail(self):
        return self.driver.find_element(*signUpElements.Email)

    def enterPassword(self):
        return self.driver.find_element(*signUpElements.Password)

    def enterConfirmPWD(self):
        return self.driver.find_element(*signUpElements.ConfirmPassword)

    def finalRegister(self):
        return self.driver.find_element(*signUpElements.RegisterButton)

    def getSuccessMessage(self):
        return self.driver.find_element(*signUpElements.SuccessMessage)

    def clickContinue(self):
        return self.driver.find_element(*signUpElements.Continue)
