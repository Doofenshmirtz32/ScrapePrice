from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.akakce.com/")
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div[3]/form/span/input")))

price = driver.find_element(By.NAME, "q")
price.send_keys("JACKSON JS11 elektro gitar")
price.send_keys(Keys.RETURN)

#WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"h1_v8")))

product = driver.find_element(By.CLASS_NAME,"pt_v8")
price_electric_guitars =product.text.splitlines()
print(f"elektro gitarların değeri {price_electric_guitars} ")
print([product.text for product in WebDriverWait(driver, 4).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "p_w_v9")))])
driver.close()
