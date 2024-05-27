import requests, json

def getData(url):
    headers = {'Content-Type': 'application/json'}
    print("Req URL: " + url)
    response = requests.get(url, verify=False, headers=headers)
    data = response.json()
    assert len(data) > 0, "empty response!"
    timeTaken = response.elapsed.total_seconds()
    return response.status_code, data, timeTaken


def postData(url, body):
    headers = {'Content-Type': 'application/json'}
    print("ReqURL:" + url)
    print("ReqBody: " + json.dumps(body))
    response = requests.post(url, verify=False, json=body, headers=headers)
    data = response.json()
   # assert len(data) > 0,"empty response!"
    timeTaken = response.elapsed.total_seconds()
    return response.status_code, data, timeTaken