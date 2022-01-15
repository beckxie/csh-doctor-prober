from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import time
import signal
import logging
import telegram

load_dotenv()

try:
    telegram_token = os.environ['telegram_token']
    telegram_chat = os.environ['telegram_chat']
    label_doctor_first_name = os.environ['label_doctor_first_name']
    label_doctor_name = os.environ['label_doctor_name']
    label_doctor_division = os.environ['label_doctor_division']
    log_path = os.environ['log_path']
    log_level = os.environ['log_level']
except:
    print("except:"+sys.exc_info()[0])
    sys.exit()

logging.basicConfig(level=log_level,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.FileHandler(log_path, 'w', 'utf-8'), ])


bot = telegram.Bot(token=(telegram_token))
docLink='https://sysint.csh.org.tw/Register/DoctorClinic.aspx'

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('/usr/bin/chromedriver',options=chrome_options)

def handler(sig, frame):
    print('Got signal: ', sig)
    browser.close()
    browser.quit()
    time.sleep(5)

signal.signal(signal.SIGTERM, handler)
signal.signal(signal.SIGINT, handler)

browser.get(docLink)

wait = WebDriverWait(browser, 10)

# click Doctor's fisrt name
element = wait.until(EC.element_to_be_clickable((By.ID,label_doctor_first_name)))
logging.info(element.text)
element.click()

# click Doctor's name
element = wait.until(EC.element_to_be_clickable((By.ID,label_doctor_name)))
logging.info(element.text)
element.click()

# click Doctor's division
element = wait.until(EC.element_to_be_clickable((By.ID,label_doctor_division)))
logging.info(element.text)
element.click()

# css selector in schedule table
sel="#DataList3 a"
while True:
    allMsg=""
    for i in range(1, 15):
        try:
            weekIdx=str(i)
            logging.info("lbWeek"+weekIdx)
            weekID="lbWeek"+weekIdx
            element = wait.until(EC.element_to_be_clickable((By.ID,weekID)))
            element.click()
            # NEEDFIX: it's a workaround for waiting element.
            time.sleep(5)

            links = browser.find_elements_by_css_selector(sel)
            for link in links:
                txt="Week"+weekIdx+","+link.text.replace("\n", "")
                # check the link is valid or not.
                if link.get_attribute("disabled"):
                    logging.debug("weeek"+weekIdx+" disabled:"+txt)
                else:
                    allMsg=allMsg+txt+"\n"
                    logging.info(txt)
                    # If it hit once on the day just break because I don't need much detail.
                    break
        except:
            logging.error("except:"+sys.exc_info()[0])
    if allMsg!="":
        bot.send_message(chat_id = "telegram_chat", text = allMsg+"\n"+docLink)
    time.sleep(1)

browser.close()
browser.quit()
time.sleep(1)
