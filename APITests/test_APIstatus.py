import pytest, json, requests
from utils import postData, getData

baseUrl = "http://localhost:5000/api"


def test_home_status():
    url = baseUrl + "/"
    body = {"email":"admin@admin","password":"1234"}
    resp_status, data, timeTaken = postData(url, body)
    assert resp_status == 401

def test_login_passstatus():
    url = baseUrl + "/login"
    body = {"email":"admin@admin","password":"1234"}
    resp_status, data, timeTaken = postData(url, body)
    assert resp_status == 200


def test_login_failstatus():
    url = baseUrl + "/login"
    body = {"email":"rns@my.cm","password":"1234"}
    resp_status, data, timeTaken = postData(url, body)
    assert resp_status == 401


def test_getAllUsers_passstatus():
    url = baseUrl + "/users"
    resp_status, data, timeTaken = getData(url)
    assert resp_status == 200


def test_getAllUsersCount_passstatus():
    url = baseUrl + "/allusercount"
    resp_status, data, timeTaken = getData(url)
    assert resp_status == 200

def test_register_existingUser():
    url = baseUrl + "/register"
    body = {"email": "admin@admin", "password": "none"}
    resp_status, data, timeTaken = postData(url, body)
    assert resp_status == 422
