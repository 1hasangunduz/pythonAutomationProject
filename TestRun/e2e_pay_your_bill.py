import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from BaseTests.Driver.driver import driver



def test_payment(driver):
    driver.get("https://newapp-staging.qlub.cloud/qr/ae/dummy-checkout/90/_/_/1827c10c80?lang=en")
    time.sleep(5)
    print("Page title is: %s" % driver.title)
    assert "Qlub" in driver.title

    # Pay The Bill button to be clickable and click on it
    pay_the_bill_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(@class, 'MuiButtonBase-root')]//span[text()='Pay now ']")))
    pay_the_bill_button.click()
    print("Pay the bill button clicked , Button Text: " + pay_the_bill_button.text)
    time.sleep(5)


    # Split Bill button to be clickable and click on it
    split_the_bill_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Split bill']")))
    split_the_bill_button.click()
    print("Split the bill button clicked, Button Text: " + split_the_bill_button.text)
    time.sleep(3)


    pay_for_your_items_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='SplitSelect_selectItem__7AiTL']//*[text()='Pay for your items']//parent::div/button")))
    pay_for_your_items_button.click()
    print("Pay for your items button clicked, Button Text: " + pay_for_your_items_button.text)
    time.sleep(3)

    # Add pay for items button to be clickable and click on it
    for i in range(1, 3):
        add_pay_for_items_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//*[@data-testid='AddRoundedIcon'])[" + str(i) + "]")))
        add_pay_for_items_button.click()
        print("Add pay for items button clicked: " + str(i) + ". item")
        time.sleep(5)

    # Confirm pay for items button to be clickable and click on it
    confirm_pay_for_items_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "split-bill")))
    confirm_pay_for_items_button.click()
    time.sleep(5)
    print("Confirm pay for items button clicked")

    # Select tip button to be clickable and click on it
    select_tip_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'TipInputs_tipScrollable')]/child::div[1]/div")))
    select_tip_button.click()
    print("Select tip button clicked, Button Text: " + select_tip_button.text)
    time.sleep(3)

    # Input card number
    input_card_number = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//iframe[@id='cardNumber']")))
    input_card_number.click()
    input_card_number.send_keys("4242424242424242")
    print("Input card number clicked and set to 4242424242424242")

    # Input card expiry date
    input_card_year = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//iframe[@id='expiryDate']")))
    input_card_year.click()
    input_card_year.send_keys("1225")
    print("Input card year clicked and set to 1225")

    time.sleep(3)

    # Input card cvv
    input_card_cvv = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//iframe[@id='cvv']")))
    input_card_cvv.click()
    input_card_cvv.send_keys("234l")
    print("Input card cvv clicked and set to 123")

    # Pay now button click on it
    button_pay_now = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Pay Now'] ")))
    button_pay_now.click()
    print("Pay now button clicked")
    time.sleep(5)

    # # Payment Successful page control
    # success_page_control = driver.find_element(By.XPATH, "//span[text()='Simulator']")
    # print("Payment Successful page opened")
    # assert "Simulator" in success_page_control.text
