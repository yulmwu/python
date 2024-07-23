from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

driver.get('https://www.mule.co.kr/mymule/mybbs')
driver.implicitly_wait(3)
driver.maximize_window()

for handle in driver.window_handles:
    if handle != driver.current_window_handle:
        driver.switch_to.window(handle)
        driver.close()  # 팝업 창 닫기

driver.switch_to.window(driver.window_handles[0])

# elements = driver.find_elements(By.CLASS_NAME, "cf")
# # for element in elements:
# #     print(element.text)
# print(elements[0].text)

# element = driver.find_element(By.XPATH, "//a[contains(text(), '뮬人/게시판')]")
# print(element.get_attribute('href'))

my_mule = driver.find_element(By.CLASS_NAME, "mymule-box")
print(my_mule.text)

driver.get_screenshot_as_file('capture_naver.png')    # 화면캡처
driver.quit() # driver 종료
