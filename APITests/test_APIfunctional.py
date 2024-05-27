import pytest, time
from utils import postData, getData

baseUrl = "http://localhost:5000/api"

testdata = [
    (["admin@admin", "1234"], 200, 422),
    (["someone@comm", "1234"], 401, 200),
]

@pytest.mark.parametrize("up,exp_login, exp_reg", testdata)
def test_login_checks(up, exp_login,exp_reg ):
    url = baseUrl + "/login"
    body = {"email": up[0], "password": up[1]}
    resp_status, data, timeTaken = postData(url, body)
    assert resp_status == exp_login
    if resp_status == 200:
        print (data['userId'])
        assert data['status'] == exp_login

@pytest.mark.parametrize("up,exp_login,exp_reg", testdata)
def test_register_checks(up,exp_login,exp_reg ):
    #time.sleep(2)
    url = baseUrl + "/register"
    body = {"email": up[0], "password": up[1]}
    if up[0] == "someone@comm":
        pytest.skip()
    resp_status, data, timeTaken = postData(url, body)
    assert resp_status == exp_reg