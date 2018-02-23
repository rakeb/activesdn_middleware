import urllib.request

import requests


def post_request(url, data, auth):
    resp = requests.post(url, json=data, auth=auth)
    return resp


def test_post():
    url = 'http://172.16.53.134:8181/restconf/operations/activesdn:subscribe-for-stats-from-switch'
    resp = requests.post(url, json={
        "input": {
            "switch-ids": [6,4]
        }
    }, auth=('admin', 'admin'))
    # resp = requests.post(url='http://172.16.53.134:8181/restconf/operations/activesdn:subscribe-for-stats-from-switch',
    #                      data={
    #                          "switch-ids": [4]
    #                      },
    #                      auth=('admin', 'admin'))
    return resp


def another_one():
    username = 'admin'
    password = 'admin'
    url = 'http://172.16.53.134:8181/restconf/operations/activesdn:subscribe-for-stats-from-switch'
    json_data = {
        "input": {
            "switch-ids": [4]
        }
    }
    passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, url, username, password)
    auth_handler = urllib.request.HTTPBasicAuthHandler(passman)
    opener = urllib.request.build_opener(auth_handler)
    urllib.request.install_opener(opener)

    data = bytes(urllib.parse.urlencode(json_data).encode())
    # req = urllib.request.Request(url, data=data)  # this will make the method "POST"
    # content = urllib.request.urlopen(req)

    handler = urllib.request.urlopen(url, data)
    print(handler.read().decode('utf-8'))

    # print(content)


if __name__ == '__main__':
    # post_request(url=None, data={}, auth=('admin','admin'))
    print(test_post())
    # another_one()