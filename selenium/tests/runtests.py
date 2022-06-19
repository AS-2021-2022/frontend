from pydoc import describe
from tracemalloc import start
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

    time.sleep(0.5)
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
    time.sleep(0.5)
    createWorkflow = None

    try:
        createWorkflow = WebDriverWait(driver , 1).until(
            lambda d: d.find_element(By.ID , "1000"))
    except:
        assert False , "Error acessing 'create workflow' tab"

    assert createWorkflow != None

    createWorkflow.click()

    time.sleep(0.5)

    submit   = driver.find_element(By.ID , "bsubmit")
    submit.click()

    try:
        alert = WebDriverWait(driver , 5).until(EC.alert_is_present())
        assert alert.text[0:6] == "Unable" 
        alert.accept()
    except:
        assert False , "Error sumbitting workflow"

    


def test_task_creation_valid():
    time.sleep(2)
    driver.find_element(By.ID , "tasks").click()



    createTask = None

    try:
        createTask = WebDriverWait(driver , 1).until(
            lambda d: d.find_element(By.ID , "1000"))
    except:
        assert False , "Error acessing 'create task' tab"

    createTask.click()

    time.sleep(1)
    name = driver.find_element(By.ID , "name")
    startDate = driver.find_element(By.ID , "startDate")
    endDate = driver.find_element(By.ID , "endDate")
    
    assignee = driver.find_element(By.ID , "assignee")
    description = driver.find_element(By.ID , "w3review")

    

    submit = driver.find_element(By.ID , "bsubmit")
    
    
    name.send_keys("valid task creation")
    startDate.send_keys("2017-06-01T08:30P")
    endDate.send_keys("2017-06-30T16:30P")

    assignee.send_keys("user3@nsn.pt")
    description.send_keys("Description test")

    time.sleep(1)

    submit.click()

    try:
        alert = WebDriverWait(driver , 5).until(EC.alert_is_present())
        assert alert.text == "task successfully created"
        alert.accept()
    except:
        assert False , "Expected alert saying 'task successfully created' from web brownser!"

def test_task_creation_invalid():
    element = driver.find_element(By.ID , "tasks")
    element.click()
    time.sleep(0.5)
    createTask = None

    try:
        createTask = WebDriverWait(driver , 1).until(
            lambda d: d.find_element(By.ID , "1000"))
    except:
        assert False , "Error acessing 'create task' tab"

    createTask.click()

    time.sleep(0.5)

    driver.find_element(By.ID , "bsubmit").click()

    try:
        alert = WebDriverWait(driver , 5).until(EC.alert_is_present())
        assert alert.text[0:6] == "Unable"
        alert.accept()

    except:
        assert False , "Expected 'alert' from web brownser"

    
def test_task_completion():
    
    task = driver.find_element(By.ID , "0")
    assert task.text == "valid task creation"
    task.click()
    time.sleep(0.5)
    conclude = driver.find_element(By.ID , "bconclude")
    assert conclude.text == "Conclude task!"

    conclude.click()

    try:
        alert = WebDriverWait(driver , 5).until(EC.alert_is_present())
        assert alert.text == "Task successfully completed!"
        alert.accept()
    except:
        assert False , "Expected 'alert' from web brownser"

