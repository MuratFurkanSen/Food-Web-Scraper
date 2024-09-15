import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

File = open("FoodNames.txt", "r")
Foods = list()
for i in File:
    Foods.append(i.strip("\n"))

conn = sqlite3.connect("Foods.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Foods ('Name', 'Portion Size','Calories', 'Nutritious')")
# Setting Up Environment
AdBlock = r"C:\Users\Fixie\PycharmProjects\FoodWebScraper\6.4.0_1"
Path = "C:/Users/Fixie/SoftwareStorage/chromedriver.exe"
Op = webdriver.ChromeOptions()
Op.add_argument("load-extension=" + AdBlock)
driver = webdriver.Chrome(options=Op)
time.sleep(10)
driver.get("https://www.nutritionvalue.org/")
driver.maximize_window()

# Creating Data
for i in Foods:
    try:
        driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/td/div[1]/a[2]").click()
        driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/form/input[1]").send_keys(i)
        driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/form/input[1]").send_keys(Keys.ENTER)
        driver.find_element(By.XPATH, "/html/body/table/tbody/tr[7]/td/table/tbody/tr[2]/td[1]/a").click()
        table = driver.find_element(By.XPATH,
                                    "/html/body/table/tbody/tr[4]/td/table/tbody/tr[4]/td[1]/table/tbody/tr/td/table/tbody")
        items = table.find_elements(By.TAG_NAME, "tr")
        portionSize = driver.find_element(By.ID, "serving-size").text
        calories = driver.find_element(By.ID, "calories").text


        raw_data = ""
        for j in items[9:-1:2]:
            part = j.find_element(By.CLASS_NAME, "left")
            if j.text.startswith(" "):
                raw_data += "-" + part.text.strip(" ")
            else:
                raw_data += "#"
                raw_data += part.text
        com = (f"INSERT INTO Foods ('Name', 'Portion Size','Calories', 'Nutritious') VALUES ('{i}','{portionSize}','{calories}','{raw_data}')")
        cur.execute(com)
        time.sleep(0.3)
    except:
        time.sleep(60)
        driver.get("https://www.nutritionvalue.org/")

driver.quit()
conn.commit()