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

serv = Service("/home/tiago/Documents/geckodriver")
driver = webdriver.Firefox(service = serv)
driver.get(commom.URL_FRONTEND)
time.sleep(2)


def assignToken():
    try:
        response = requests.request('GET' , commom.URL_BACKEND + "login?username=user3&password=3").json()
    except:
        assert False, "error talking to the server"
    assert response["token"] != None
    TOKEN = response["token"]

def test_loginUI():
    
    user = driver.find_element(By.ID , "user")
    user.send_keys("user3")

    password = driver.find_element(By.ID , "pass")
    password.send_keys("password3")

    button = driver.find_element(By.CLASS_NAME , "btn")
   
    button.click()
    
    try:
        element = WebDriverWait(driver , 20).until(
            lambda d: d.find_element(By.TAG_NAME , "img")
        )
        

    except:
        assert False , "Login took too much time or authentication proccess failed"
            
    assert True


def test_workflow_creation():
    element = driver.find_element(By.ID , "workflows")
    element.click()

    createWorkflow = None

    try:
        createWorkflow = WebDriverWait(driver , 1).until(
            lambda d: d.find_element(By.ID , "1000"))
    except:
        assert False , "Error acessing 'create workflow' tab"

    assert createWorkflow != None

    createWorkflow.click()

    






