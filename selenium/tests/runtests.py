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


def test_workflow_creation_valid():
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

    time.sleep(0.1)
    wname = driver.find_element(By.ID , "wname")

    wname.send_keys("workflow name test")

    nextStep = driver.find_element(By.ID , "bnstep")
    submit   = driver.find_element(By.ID , "bsubmit")

    nextStep.click()

    a0 = driver.find_element(By.ID , "a0")
    a0.send_keys("user3@nsn.pt")

    d0 = driver.find_element(By.ID , "d0")
    d0.send_keys("Workflow description text")

    submit.click()

    try:
        WebDriverWait(driver , 5).until(
            lambda d: d.find_element(By.ID , "0")
        )
    except:
        assert False, "error submitting workflow"
        

def test_workflow_creation_invalid():

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

    submit   = driver.find_element(By.ID , "bsubmit")
    submit.click()

    try:
        alert = WebDriverWait(driver , 5).until(EC.alert_is_present())
        assert alert.text[:6] == "Unable" 
    except:
        assert False , "Error sumbitting wrong "

    