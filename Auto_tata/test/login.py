import json
import pytest
import requests



def test_login():
    headers = {'Content-Type': 'application/json'}
    url = 'https://crm-api.rtmap.com/crmapi/access/auth/login'
    data = {
        "customer_code": "zhihuitu",
        "company_code": "zhihuitu",
        "user_code": "admin",
        "user_password": "RRtmap911",
        "router_path": "/login"
    }
    dataJson = json.dumps(data)  # 将 dict转成str
    requests.packages.urllib3.disable_warnings()
    return_st = requests.post(url, data=dataJson, headers=headers, verify=False)
    rj = return_st.json()
    token = rj['data']['token']
    print(rj['status'], rj['message'])
    if rj['status'] == 200:
        print("CRM系统 登录成功")
        print("token为", token)
    assert rj['status'] == 200 and rj['message'] == '请求成功'
    return token


def test_001():
    x = "hello"
    print(x)
    assert "h" in x


def test_002():
    x = "hello"
    print(x, '您好')
    assert "he" in x



if __name__ == "__main__":
    # pytest.main(["-q", "../test/login.py"])
    pytest.main(["-q", "../test/login.py", "../test/run_email.py", '-v', '--html=../report/all_report.html', '--self'
                                                                                                             '-contained-html'])
