import json
import requests
import case.vip_info.login as login

token = login.test_login()


def test_findvipinfo():
    headers = {'Content-Type': 'application/json'}
    url = 'https://crm-api.rtmap.com/crmapi/member/operate/getMemberPoints'
    data = {"token": token, "vip_uid": "F0BE863DD5058D691CEB2CB020786C71", "router_path": "/vip/vip_workbench"}
    dataJson = json.dumps(data)  # 将 dict转成str
    requests.packages.urllib3.disable_warnings()
    res = requests.post(url=url, data=dataJson, headers=headers, verify=False)
    json.loads(res.text)

    s = requests.session()
    s.keep_alive = False

    code = res.status_code
    if code == 200:
        print("会员查询成功")
        # print("vip_uid:", data.get("vip_uid"))