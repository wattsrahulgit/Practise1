import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from PageObjectModels import Objects
from PageObjectModels.Objects import ApplicationElements
from utilities.ElementLocators import ElementLocators


class TestDemoWebApp(ElementLocators):

    def test_Practise1(self):
        testDemo = Objects.ApplicationElements(self.driver)

        testDemo.getComputers().click()
        testDemo.getDesktops().click()
        testDemo.getOrderBy().click()
        options = testDemo.getSortBy()
        options[3].click()
        BottomOfPage = testDemo.getCustomerService()
        testDemo.MoveElement(BottomOfPage)
        testDemo.getExpensiveDesktop().click()
        assert testDemo.checkFreeShip().is_displayed()
        testDemo.checkSearchItems().send_keys(Keys.PAGE_DOWN)

        Configuration = testDemo.selectConfig()
        Configuration[2].click()
        Configuration[5].click()
        Configuration[7].click()

        SoftwareSelect = testDemo.selectSoftware()
        SoftwareSelect[2].click()

        testDemo.EnterQuantity().clear()
        testDemo.EnterQuantity().send_keys("4")
        testDemo.CartValue().click()
        time.sleep(3)
        testDemo.ScrollUp()
        testDemo.FinalCart().click()

        GiftCard = testDemo.AddGift()
        testDemo.MoveElement(GiftCard)

        SelectCountry = testDemo.selectCountry()
        SelectCountry.select_by_visible_text("Canada")
        time.sleep(2)

        SelectProvince = testDemo.selectProvince()
        SelectProvince.select_by_visible_text("Manitoba")

        # testDemo.ShippingEstimation().click()

        Buttons = testDemo.getCommonButtons()
        Buttons.location_once_scrolled_into_view

        testDemo.selectAgreement().click()
        testDemo.FinalCheckout().click()
        testDemo.ContinueGuest().click()
        testDemo.clickContinue().click()
        time.sleep(2)
        ErrorMessage = testDemo.ErrorMessageCheck().text
        print(ErrorMessage)
        assert ErrorMessage == "First name is required."

