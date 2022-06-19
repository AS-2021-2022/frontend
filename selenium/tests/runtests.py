from selenium import webdriver
import pytest
import time
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import commom
import selenium
import requests

TOKEN = None

def test_loginUI():
    serv = Service("/home/tiago/Documents/geckodriver")

    driver = webdriver.Firefox(service = serv)

    driver.get(commom.URL_FRONTEND)

    time.sleep(2)
    user = driver.find_element(By.ID , "user")
    user.send_keys("user1")

    password = driver.find_element(By.ID , "pass")
    password.send_keys("password1")

    button = driver.find_element(By.CLASS_NAME , "btn")
   
    button.click()
    
    try:
        element = WebDriverWait(driver , 20).until(
            lambda d: d.find_element(By.TAG_NAME , "img")
        )
        

    except:
        assert False , "Login took too much time or authentication proccess failed"
            
    
    assert True

def test_loginRQ():
    time.sleep(1)
    try:
        response1 = requests.request('GET' , commom.URL_BACKEND + "login?username=wrong&password=wrong").json()
        response2 = requests.request('GET' , commom.URL_BACKEND + "login?username=user1&password=password1").json()
    except:
        assert False, "error talking to the server"

    assert response1["status"] == "rejected"
    assert response2["status"] == "accepted"

    assert response2["token"] != None

    TOKEN = response2["token"]

def test_getWorkflows():
    time.sleep(1)
    
    response = requests.request('GET' , commom.URL_BACKEND + "getWorkflows?token=" + TOKEN).json()
    

    assert response["status"] == "accepted"

    assert response["workflows"] != None

def test_getTasksList():
    time.sleep(1)
    try:
        response = requests.request('GET' , commom.URL_BACKEND + "getTasksList?token=" + TOKEN).json()
    except:
        assert False, "error talking to the server"

    assert response["status"] == "accepted"

    assert response["tasks"] != None

test_loginRQ()
test_getTasksList()