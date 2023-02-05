from json import dumps
import requests
import assertpy
from assertpy import assert_that, soft_assertions
import logging
import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import CustomerLogger



def test_Create_New_ToDo_Task():
    log = CustomerLogger.LogGen()
    log.info("Start of the script execution")
    Payload = Create_Payload()
    RAW_Created_Task_response = Create_New_ToDo_Task(Payload)
    JSON_Created_Task_response = RAW_Created_Task_response.json()
    with soft_assertions():
        assert_that(RAW_Created_Task_response.status_code).is_equal_to(200)
        assert_that(JSON_Created_Task_response["task"]["user_id"]).is_equal_to(Payload["user_id"])
    log.info("End of the script execution")

def test_Get_Task_details():
    Payload = Create_Payload()
    RAW_Task_Details_response = Create_New_ToDo_Task(Payload)
    JSON_Task_Details_response= RAW_Task_Details_response.json()
    with soft_assertions():
        assert_that(RAW_Task_Details_response.status_code).is_equal_to(200)
        assert_that(Payload["user_id"]).is_equal_to(JSON_Task_Details_response["task"]["user_id"])



def test_List_Tasks_Created():
    _, _, Task_Id, User_Id = Create_New_ToDo_Task()
    JSON_Task_Details_response, RAW_Task_Details_response = Get_Task_Details(Task_Id)
    RAW_List_Tasks_response = requests.get(ReadConfig.getBaseURL() + 'list-tasks/' + User_Id)
    JSON_List_Tasks_response = RAW_List_Tasks_response.json()


def test_Update_Task():
    _, _, Task_Id, User_Id = Create_New_ToDo_Task()
    Update_Task_Pay = Update_Task_Payload(Task_Id)
    RAW_Update_Task = requests.put(ReadConfig.getBaseURL()+ '/update-task', json=Update_Task_Pay)
    JSON_Update_Task = RAW_Update_Task.json()
    with soft_assertions():
        assert_that(RAW_Update_Task.status_code).is_equal_to(200)








def Get_Task_Details(Task_Id):
    return requests.get(ReadConfig.getBaseURL() + 'get-task/' + Task_Id)


def Create_New_ToDo_Task(Payload):
    return requests.put(ReadConfig.getBaseURL() + 'create-task', json=Payload)


def Create_Payload():
    return {
    "content": "Comb Hair",
    "user_id": "VinayVibhuti",
    "is_done": False
    }


def Update_Task_Payload(Task_id):
    return {
    "content": "Comb Hair and Clean face",
    "user_id": "VinayVibhuti",
    "task_id": Task_id,
    "is_done": False
    }