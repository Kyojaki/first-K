from pydoc import classname
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

url = "https://alwayzseller.ilevit.com/"

options = Options()
options.add_argument("--start-maximized")  # 화면 최대화
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get(url)  # 페이지 열기

time.sleep(1)

# 아이디 입력창
id = driver.find_element(By.NAME, "name")
id.click()
id.send_keys("ysetin")

# 비밀번호 입력창
pw = driver.find_element(By.NAME, "password")
pw.click()
pw.send_keys("khslove78@")

# 로그인 버튼 클릭
# login_btn = driver.find_element(By.XPATH, '//*[//*[@id="root"]/div/div/button[1]]')
# login_btn.click()
